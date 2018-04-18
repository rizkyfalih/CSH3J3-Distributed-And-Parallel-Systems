# NAMA : NAUFAL IHSAN KUSUMAYADHI
# KELAS : IF-39-01
# NIM : 1301154409
import math
import xlrd
import xlsxwriter
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d

def open_file(path) :
    book = xlrd.open_workbook(path) # buka file excel, path adalah nama filenya harus se folder
    # book2 = xlsxwriter.Workbook('JAWABAN TUGAS 1.3.xlsx')
    book2 = open("prediksi.txt", "w")
    sheet1 = book.sheet_by_index(0) # sheet1 diisi oleh book sheet pertama
    sheet2 = book.sheet_by_index(1) # sheet2 diisi oleh book sheet kedua
    # sheettest = book2.add_worksheet()
    return sheet1, sheet2, book2 # mengembalikan sheet1 dan sheet2

def cekpoint(sheet) : # input merupakan sebuah sheet yang akan dilakukan proses kfold untuk memperoleh perkiraan akurasi sistem
    prediksi = [] # array untuk menampung hasil prediksi atribut class atau y
    x = 0 # index untuk acuan sedang mengakses baris yang mana
    while (x < 50) : # proses K-Fold dimana data baris ke 1-50 menjadi data test
        sum1, sum2, sum3 = sumLayerKFold(patternLayerKFold(sheet.row_values(x),sheet,50,149), sheet, 50,149) # melakukan layer pattern, sum, dan menyimpan langsung ke dalam 3 nilai, lihat detail komentar function
        prediksi.append(outputLayer(sum1, sum2, sum3)) # mengisi array prediksi
        x += 1
    while (x < 100) :  # proses K-Fold dimana data baris ke 51-100 menjadi data test
        sum1, sum2, sum3 = sumLayerKFoldsbg(patternLayerKFoldsbg(sheet.row_values(x),sheet,0,49,100,149), sheet, 0,49,100,149)
        prediksi.append(outputLayer(sum1, sum2, sum3))
        x += 1
    while (x < 150) : # proses K-Fold dimana data baris ke 101-150 menjadi data test
        sum1, sum2, sum3 = sumLayerKFold(patternLayerKFold(sheet.row_values(x),sheet,0,99), sheet, 0,99)
        prediksi.append(outputLayer(sum1, sum2, sum3))
        x += 1
    x = 0
    poin = 0
    # print(prediksi)
    while (x < 150) : # mencocokan hasil prediksi dengan atribut class atau y nya di setiap baris
        if (prediksi[x] == sheet.row_values(x)[3]) : # apabila sama, menambah poin sebanyak 1
            poin += 1
        # print(prediksi[x],sheet.row_values(x)[3])
        x += 1
    print("Benar", poin, "dari 150 data train")
    print("Perkiraan Akurasi dari data train =",((poin/150)*100),"%") #print presentase

def patternLayerKFold(testrow,trainsheet,start,end) : # mencari hasil fungsi g(x) dari sebuah row data terhadap seluruh row dari sebuah sheet dimulai dari baris ke start berakhir di baris ke end
    smooth = pow(1.5,2) # nilai smoothing setelah dikuadratkan
    i = start
    gx = []
    while (i <= end) :
        pangkat = -1*(pow(testrow[0] - trainsheet.cell(i,0).value,2) + pow(testrow[1] - trainsheet.cell(i,1).value,2) + pow(testrow[2] - trainsheet.cell(i,2).value,2))/(2*smooth) # isi pangkat dari exponen rumus gaussian
        gx.append(np.exp(pangkat)) # memasukkan hasil perhitungan terhadap tiap baris data train menjadi g(x)
        i += 1
    return gx

def patternLayerKFoldsbg(testrow,trainsheet,start1,end1,start2,end2) : # mencari hasil fungsi g(x) dari sebuah row data terhadap seluruh row dari sebuah sheet tetapi loncat, dimulai dari baris ke start1 berakhir di baris ke end1, kemudian dimulai kembali dari start2 dan berakhir di end2
    smooth = pow(1.5,2) # nilai smoothing setelah dikuadratkan
    i = start1
    gx = []
    while (i <= end1) :
        pangkat = -1*(pow(testrow[0] - trainsheet.cell(i,0).value,2) + pow(testrow[1] - trainsheet.cell(i,1).value,2) + pow(testrow[2] - trainsheet.cell(i,2).value,2))/(2*smooth) # isi pangkat dari exponen rumus gaussian
        gx.append(np.exp(pangkat)) # memasukkan hasil perhitungan terhadap tiap baris data train menjadi g(x)
        i += 1
    i = start2
    while (i <= end2) :
        pangkat = -1*(pow(testrow[0] - trainsheet.cell(i,0).value,2) + pow(testrow[1] - trainsheet.cell(i,1).value,2) + pow(testrow[2] - trainsheet.cell(i,2).value,2))/(2*smooth) # isi pangkat dari exponen rumus gaussian
        gx.append(np.exp(pangkat)) # memasukkan hasil perhitungan terhadap tiap baris data train menjadi g(x)
        i += 1
    return gx

def sumLayerKFold(gx, sheet, start, end) : # menjumlahkan dan merata-ratakan nilai g(x) di setiap classnya
    sum1 = 0
    sum2 = 0
    sum3 = 0
    jml1 = 0
    jml2 = 0
    jml3 = 0
    i = start
    j = 0
    while (i <= end) : # memilah penjumlahan tergantung dari class y data trainnya
        if (sheet.row_values(i)[3] == 0) :
            sum1 += gx[j]
            jml1 += 1
        elif (sheet.row_values(i)[3] == 1.0) :
            sum2 += gx[j]
            jml2 += 1
        elif (sheet.row_values(i)[3] == 2.0) :
            sum3 += gx[j]
            jml3 += 1
        i += 1
        j += 1
    i = 0
    sum1 = sum1/jml1
    sum2 = sum2/jml2
    sum3 = sum3/jml3
    return sum1,sum2,sum3

def sumLayerKFoldsbg(gx, sheet, start1, end1, start2, end2) : # menjumlahkan dan merata-ratakan nilai g(x) di setiap classnya, tetapi loncat
    sum1 = 0
    sum2 = 0
    sum3 = 0
    jml1 = 0
    jml2 = 0
    jml3 = 0
    i = start1
    j = 0
    while (i <= end1) : # memilah penjumlahan tergantung dari class y data trainnya
        if (sheet.row_values(i)[3] == 0) :
            sum1 += gx[j]
            jml1 += 1
        elif (sheet.row_values(i)[3] == 1.0) :
            sum2 += gx[j]
            jml2 += 1
        elif (sheet.row_values(i)[3] == 2.0) :
            sum3 += gx[j]
            jml3 += 1
        i += 1
        j += 1
    i = start2
    while (i <= end2) : # memilah penjumlahan tergantung dari class y data trainnya
        if (sheet.row_values(i)[3] == 0) :
            sum1 += gx[j]
            jml1 += 1
        elif (sheet.row_values(i)[3] == 1.0) :
            sum2 += gx[j]
            jml2 += 1
        elif (sheet.row_values(i)[3] == 2.0) :
            sum3 += gx[j]
            jml3 += 1
        i += 1
        j += 1
    sum1 = sum1/jml1
    sum2 = sum2/jml2
    sum3 = sum3/jml3
    return sum1,sum2,sum3

def outputLayer(sum1, sum2, sum3) : # mencari nilai sum mana yang lebih besar dari setiap classnya untuk menentukan prediksi class di row tersebut
    if ((sum1 > sum2) and (sum1 > sum3)) :
        return(0.0)
    elif ((sum2 > sum1) and (sum2 > sum3)) :
        return(1.0)
    elif ((sum3 > sum1) and (sum3 > sum2)) :
        return(2.0)

def showPlot(train) : # menampilkan visualisasi distribusi data train
    i = 0
    x1class0 = []
    x2class0 = []
    x3class0 = []
    x1class1 = []
    x2class1 = []
    x3class1 = []
    x1class2 = []
    x2class2 = []
    x3class2 = []
    while (i < 150) :
        if (train.row_values(i)[3] == 0.0) : # apabila atribut kolom ke-4 nya = 0.0, dimasukkan ke array untuk atribut2 class 0
            x1class0.append(train.row_values(i)[0])
            x2class0.append(train.row_values(i)[1])
            x3class0.append(train.row_values(i)[2])
        elif (train.row_values(i)[3] == 1.0) : # apabila atribut kolom ke-4 nya = 0.0, dimasukkan ke array untuk atribut2 class 1
            x1class1.append(train.row_values(i)[0])
            x2class1.append(train.row_values(i)[1])
            x3class1.append(train.row_values(i)[2])
        elif (train.row_values(i)[3] == 2.0) : # apabila atribut kolom ke-4 nya = 0.0, dimasukkan ke array untuk atribut2 class 2
            x1class2.append(train.row_values(i)[0])
            x2class2.append(train.row_values(i)[1])
            x3class2.append(train.row_values(i)[2])
        i += 1
    return x1class0,x2class0,x3class0,x1class1,x2class1,x3class1,x1class2,x2class2,x3class2

def prediksiTest(test, train, jawaban) : # mencari prediksi output dari data train yang hasil nya disimpan dalam array jawaban
    prediksi = []
    i = 0
    sum1 = 0
    sum2 = 0
    sum3 = 0
    print("HASIL PREDIKSI DATA TEST")
    while (i < 30) :
        sum1, sum2, sum3 = sumLayerKFold(patternLayerKFold(test.row_values(i),train,0,149), train, 0,149) # melakukan layer pattern, sum, dan menyimpan langsung ke dalam 3 nilai, lihat detail komentar function
        prediksi = outputLayer(sum1, sum2, sum3) # mengisi array prediksi
        jawaban.write(str(outputLayer(sum1, sum2, sum3)))
        jawaban.write("\t")
        print("BARIS KE-",i+1,prediksi)
        i += 1
    jawaban.close()
    print("FILE SUDAH DI WRITE")

def main() : # function yang paling pertama di jalankan
    train,test,jawaban = open_file("data_train_PNN.xlsx") # memasukkan file input menjadi 3 buah variabel yang isinya berupa sheet dari excel
    fig = plt.figure() # dari sini
    ax1 = fig.add_subplot(111, projection = '3d') # ini juga
    x1class0,x2class0,x3class0,x1class1,x2class1,x3class1,x1class2,x2class2,x3class2 = showPlot(train) # ini juga
    ax1.scatter(x1class0,x2class0,x3class0, label = 'Class 0', c = 'r') # ini juga
    ax1.scatter(x1class1,x2class1,x3class1, label = 'Class 1',  c = 'g') # ini juga
    ax1.scatter(x1class2,x2class2,x3class2, label = 'Class 2', c = 'b') # ini juga
    ax1.set_xlabel('x1') # ini juga
    ax1.set_ylabel('x2') # ini juga
    ax1.set_zlabel('x3') # ini juga
    plt.title('Visualisasi Distribusi Data Train') # ini juga
    plt.legend() # ini juga
    plt.show() # sampai sini adalah proses menampilkan grafik
    cekpoint(train) # deskripsi function ada di function nya
    prediksiTest(test, train, jawaban) # deskripsi function ada di function nya
    print("SELESAI")

main() # prediksi dalam function cekpoint2 masih hanya 1 record, belum disesuaikan data mana yang akan di test terhadap data yang mana
