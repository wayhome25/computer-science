import socket


s = socket.socket()
host = socket.gethostname()
port = 12222

s.connect((host, port))
print( 'Connected to', host)

while True:
    z = input("Enter something for the server: ")
    s.send(z.encode('utf-8'))
    # Halts
    print ('[Waiting for response...]')
    print ((s.recv(1024)).decode('utf-8'))
