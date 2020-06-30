#coding:utf-8
import socket
import handshake
import time

HOST = '0.0.0.0'
PORT = 7777

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind((HOST, PORT))

s.listen(1)

print('socket start')

clients = 0
while True:
    conn, addr = s.accept()
    clients += 1
    print('Connected by ', addr)
    data = conn.recv(1024).decode()
    hs = handshake.HandShake()
    hs.parse_msg(data)

print('socket stop')
exit(0)
            