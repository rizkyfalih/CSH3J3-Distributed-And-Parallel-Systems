import xmlrpc.client
import pandas as pd
from io import StringIO
import io

server = xmlrpc.client.ServerProxy('http://10.20.32.69:8000', allow_none=True)

# Load data
X_train = []
X_train.append(['Chinese', 'Beijing', 'Chinese']) 
X_train.append(['Chinese', 'Chinese', 'Shanghai'])
X_train.append(['Chinese', 'Macao'])
X_train.append(['Tokyo', 'Japan', 'Chinese'])

y_train = ['c','c','c','j']

label_list = list(set(y_train))

prior = server.prior(y_train, label_list)

print(prior)