import socket

print('Client Started....')

def Main():
    
    #FOR HOST, USE THE SERVER IPV4 FROM IPCONFIG
    host = '127.0.0.1'
    port = 5050
    
    mySocket = socket.socket()
    mySocket.connect((host,port))
    
    
    message = input('--> ')
    
    while message != 'q':
        mySocket.send(message.encode())
        data = mySocket.recv(1024).decode()
        
        print ('Received from Server: ' + data)
        
        message = input('--> ')
        
    mySocket.close()
    
    
if __name__ == '__main__':
    Main()
