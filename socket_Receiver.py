#!/usr/bin/python
import socket
import commands
x = socket.socket( socket.AF_INET , socket.SOCK_DGRAM )
x.bind(("192.168.122.1",1140))
x.recvfrom(100)
