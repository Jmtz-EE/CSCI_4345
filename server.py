#we need socket tools
from socket import *


#create a socket object 
serverSocket = socket(AF_INET, SOCK_DGRAM)

#bind it 
#serverSocket.bind( ('127.0.0.1',12345) )
serverSocket.bind( ('0.0.0.0',12345) )

#change this, so  that we receive msg continually 
    #if msg is "exit", you can exit 

#TASK 1: give your server any custom behavior 


#Task 2a : Use your server to send a reply to client address

#recv messege

while True:
    #recv messege
    msg, clientAddr = serverSocket.recvfrom(2048) #asks for the buffer size to know when to stop reading 
    print(msg.decode())

    if msg.decode() == 'exit':
        break