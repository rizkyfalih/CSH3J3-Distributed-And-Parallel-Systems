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
with SimpleXMLRPCServer(("10.20.32.69", 8000),
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

    def prior_probability(y, y_list):
        p = [0] * len(y_list)
        for i in range(len(y_list)):
            for j in range(len(y)):
                if y_list[i] == y[j]:
                    p[i] +=1
        total_p =sum(p)
        for i in range(len(p)):
            p[i]/=total_p
        return p

    server.register_function(prior_probability, 'prior')

    # Run the server's main loop
    server.serve_forever()