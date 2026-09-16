from socket import *

#create socket 
clientSocket = socket(AF_INET, SOCK_DGRAM)


#change this, so that we keep sending messages 
#   make the messages different every time 
#create a message


#TASK ) send to a friend is stead of own 


#Task 2 b: Recieve a reply from the server after sending 
while True: 
    #create a message 
    msg = input('msg to send\n')

    #turn this into bytes for the buffer 
    msg = msg.encode()

    #send the messege # go back to 127.0.0.1
    clientSocket.sendto(msg, ('172.28.140.55', 12345))

    if msg.decode() == 'exit':
        break

#Tidy up - close the socket 
clientSocket.close()
