from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer

authorizer = DummyAuthorizer()
authorizer.add_user("liyihang", "liyihang", ".", perm="elradfmw")
handler = FTPHandler
handler.authorizer = authorizer
server = FTPServer(("111.186.114.69",21),handler)
server.serve_forever()