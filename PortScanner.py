

import socket
import time

print('Thanks for using Jacks Port Scanner')
time.sleep(2)

s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

start = True

    
def portScanner():

    
    host= 0
    port= 0
    
    while port == 0 and host == 0:
        
        host = str(input('Please choose IP Address: \n'))
        time.sleep(2)
        port = int(input('Please choose a Port: \n'))
        time.sleep(2)
        print('Scanning.....')
        time.sleep(4)
    
    if s.connect_ex((host, port)):
        print('The Port is Closed!')
        time.sleep(3)
    else:
        print('The Port is open! \n')
        time.sleep(3)
        
        
while start:
    
    portScanner()
        
        

        
        
