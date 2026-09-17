#we need socket tools
from socket import *


#create a socket object 
serverSocket = socket(AF_INET, SOCK_DGRAM)

#bind it 
#serverSocket.bind( ('127.0.0.1',12345) ) 
#why 0.0.0.0
serverSocket.bind( ('127.0.0.1',12345) )

#change this, so  that we receive msg continually 
    #if msg is "exit", you can exit 

#TASK 1: give your server any custom behavior 
#custom behavior - make it so the server can make all caps received message

def capatilize(input):
    return input.upper()


#Task 2a : Use your server to send a reply to client address

while True:
    #recv messege
    msg, clientAddr = serverSocket.recvfrom(2048) #asks for the buffer size to know when to stop reading 
    print(msg.decode())
    
    msg2 = capatilize(msg.decode())
    
    #adding clientAddr[0].encode() makes it go from '127.0.0.1' to b'127.0.0.1' 
    serverSocket.sendto(msg2.encode(), clientAddr )#we are receiving bytes so this should send 
    #why are we using 12345
    if msg.decode() == 'exit':
        break