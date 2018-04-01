import xmlrpc.client
import pandas as pd
from io import StringIO
import io

server = xmlrpc.client.ServerProxy('http://192.168.1.5:8000', allow_none=True)

# Load data
dataTrain = pd.read_csv('data_train_PNN.txt', delimiter = "\t").round(9)
dataTrain = StringIO(dataTrain)

print(dataTrain)
# z1 = dataTrain.loc[1, 'att1':'att3']
# z2 = dataTrain.loc[:, 'att1':'label']

# sigmas = {0:1, 1:1, 2:1}
# z3 = server.patternLayer(z1, z2, sigmas)
