import socket

url = input("Enter an URL: ")

try :  
    host = url.split('/')
    dom = host[2]
    mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    mysock.connect((dom , 80))
    cmd = f'GET {url} HTTP/1.0\r\n\r\n'.encode()
    mysock.send(cmd)
except :
    print("Unvalid URL")
    quit()

count = 0

while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    else: 
        count = count + len(data)
    if count <= 3000:
           print(data.decode(),end='')

mysock.close()

print("\nTotal Count:" , count) # \n forces to cursor to jump to a new line. 
