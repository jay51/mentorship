import socket as sock
import sys, select

s = sock.socket(sock.AF_INET, sock.SOCK_STREAM, 0)
# addr = ('192.168.0.87', 80)
addr = ('127.0.0.1', 8888)
s.setsockopt(sock.SOL_SOCKET, sock.SO_REUSEADDR, 1)

s.bind(addr)
s.listen()

while True:
    conn, addr = s.accept()
    print('Connected ', addr)

    # breakpoint()
    while True:
        rlist, o, e = select.select( [sys.stdin, conn], [], [], 2)

        if conn in rlist:
            # conn.recv is blocking 
            data = conn.recv(512).decode()
            print('recived data: ', data)

        if sys.stdin in rlist:
            # stdin.readline is blocking 
            buff = sys.stdin.readline().strip()
            rtn = conn.send("user said: ".encode() + buff.encode() + b'\n')
            print('sent: ', buff, ' size: ', rtn)

            

def modified_input(st, timeout):
    import signal
    def interrupted(signum, frame):
        # print('interrupted!')
        raise Exception('exit')

    TIMEOUT = timeout # number of seconds your want for timeout
    signal.signal(signal.SIGALRM, interrupted)

    # set alarm
    signal.alarm(TIMEOUT)
    try:
        print('You have 5 seconds to type in your stuff...')
        result = input(st)
        return result
    except Exception as e:
        # print(e)
        pass

    # disable the alarm after success
    signal.alarm(0)
    return ''

#username = modified_input('username: ', 3)
#print('You typed', username)




