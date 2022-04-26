#!/usr/bin/python3
import socket
from _thread import *
import threading
import random


text="redacted"
flag="redacted"
seed="redacted" #but you won't guess it during the ctf, look somewhere else
i=0

def threaded(c):
    global i
    while True:

        data = c.recv(1024)
        if not data:
             break

        rand=str(random.randrange(10E9,10E10))
        if data.decode('utf-8')==rand:
            c.send((text + flag).encode('utf-8'))
        else:
            sendingData="id: {}\nrand: {}\nWhat's the next random number?\n".format(i,rand)
            c.send(sendingData.encode('utf-8'))
        i+=1
    c.close()


def Main():
    random.seed(seed)
    host = "0.0.0.0"
    port = 31337
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, port))
    s.listen()
    while True:
        c, addr = s.accept()
        start_new_thread(threaded, (c,))
    s.close()


if __name__ == '__main__':
    print("Starting random number generator")
    Main()
