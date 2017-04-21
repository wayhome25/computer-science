import socket


s = socket.socket()
host = socket.gethostname()
port = 12222
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((host, port))

s.listen(5)
c = None

while True:
   if c is None:
       # Halts
       print( '[Waiting for connection...]')
       c, addr = s.accept() #  (socket object, address info) return
       print( 'Got connection from', addr)
   else:
       # Halts
       print( '[Waiting for response...]')
       print((c.recv(1024)).decode('utf-8'))
       q = input("Enter something to this client: ")
       c.send(q.encode('utf-8'))
