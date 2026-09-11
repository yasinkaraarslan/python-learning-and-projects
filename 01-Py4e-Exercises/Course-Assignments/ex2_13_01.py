import urllib.request

from bs4 import BeautifulSoup 

url = input("Enter an URL: ")

try:
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('p')
    print(len(tags))
except:
    print("Unvalid URL")
    