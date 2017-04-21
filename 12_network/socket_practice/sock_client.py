import socket
import sys

if __name__=='__main__':
    # try to create socket
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except socket.error as e:
        print('Failed')
        print('reason:{}'.format(str(e)))
        sys.exit(); # 강제로 스크립트 종료 

    print('socket created')

    # get host, port from user
    host = input('Enter host: ')
    post = input('Enter post: ')

    #try to connect to host, port and shutdown socket 
    try:
        sock.connect((host, int(port)))
        print('socket connected!')
        sock.shutdown(2)
    except socket.error as err:
        print('Failed..')
        print('Reason: ', str(err))
        sys.exit();
        
