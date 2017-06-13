
#!/usr/bin/python
import socket
import commands
x= socket.socket( socket.AF_INET , socket.SOCK_DGRAM )
message=raw_input("Enter text: ")
x.sendto(message,("192.168.122.22",1140))
