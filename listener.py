import socket
import sys

def recv():
    s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_ICMP)
    while True:
        data, src = s.recvfrom(1508)
        payload = data[44:60]
        sys.stdout.write(payload)


if __name__ == '__main__':
    recv()
