import socket
import sys


if __name__=='__main__':
    try:
        sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        #tpc를 이용해서 소켓을 생성한다. 
    except socket.error as e:
        print('failed')
        print('reason: {}'.format(str(e)))
        sys.exit();

    print('socket created')

    host = input('Enter host:')
    port = input('Enter post:')

    try:
        sock.connect((host, int(port)))
        print('socket connected')
        sock.shutdown(2)
        # 2 : 서버, 클라이언트 모두 종료 

    except socket.error as err:
        print('failed')
        print('Reason', str(err))
        sys.exit();



