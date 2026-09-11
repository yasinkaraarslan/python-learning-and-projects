import urllib.request

url = input("Enter an URL: ")

count = 0

try:
    fhand = urllib.request.urlopen(url)
    for line in fhand :
        data = line.decode()
        count = count + len(data)
        if count <= 3000:
              print(data, end='')
    print(count)
except:
    print("Unvalid URL")
    quit()
    


