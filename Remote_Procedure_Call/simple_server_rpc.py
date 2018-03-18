from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler

# Restrict to a particular path.
class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

# Create server
with SimpleXMLRPCServer(("192.168.1.8", 8000),
                        requestHandler=RequestHandler) as server:
    server.register_introspection_functions()

    # Register pow() function; this will use the value of
    # pow.__name__ as the name, which is just 'pow'.
    server.register_function(pow)
    server.register_function(sum)

    # Register a function under a different name
    def adder_function(x,y):
        return x + y
    server.register_function(adder_function, 'add')

    # Register an instance; all the methods of the instance are
    # published as XML-RPC methods (in this case, just 'mul').
    class MyFuncs:
        def mul(self, x, y):
            return x * y

    server.register_instance(MyFuncs())

    # Run the server's main loop
    server.serve_forever()

##from xmlrpc.server import SimpleXMLRPCServer
##
##address = ('localhost', 50000)
##server = SimpleXMLRPCServer(address)
##
##
##def multiply(a, b):
##    """return the product of two numbers"""
##    return a * b
##server.register_function(multiply)
##
##
##if __name__ == '__main__':
##    try:
##        print ("Server running on %s:%s" % address)
##        #print "Use Ctrl-C to Exit"
##        server.serve_forever()
##    except KeyboardInterrupt:
##        server.server_close()
##        print ("Exiting")