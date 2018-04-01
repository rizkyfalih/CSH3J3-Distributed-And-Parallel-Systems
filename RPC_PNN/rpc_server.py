from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler

#import library
import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as pyplot
from numpy import linalg as la
from io import StringIO
import io

class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

# Create server
with SimpleXMLRPCServer(("192.168.1.5", 8000),
                        requestHandler=RequestHandler) as server:
    server.register_introspection_functions()

    # Register a function
    def g_function(x, sigma, w):
        y = x.sub(w, axis = 0) 
        y = la.norm(y.values)
        return np.exp(-y / (2*sigma)**2)

    server.register_function(g_function, 'g')

    def patternL(data, dataTrain, sigma_dict):
        for i in dataTrain.index:
            this_label = int(dataTrain.loc[i, 'label'])
            dataTrain.loc[i, 'sigma'] = sigma_dict[this_label]
            dataTrain.loc[i,'g'] = g_function(data, sigma_dict[this_label], dataTrain.loc[i, 'att1':'att3'])
        return dataTrain

    server.register_function(patternL, 'patternLayer')

    # Run the server's main loop
    server.serve_forever()