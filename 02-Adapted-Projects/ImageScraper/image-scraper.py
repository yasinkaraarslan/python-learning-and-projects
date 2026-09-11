import urllib.request 

from bs4 import BeautifulSoup 

import ssl 
ctx = ssl.create_default_context()
ctx.check_hostname = False 
ctx.verify_mode = ssl.CERT_NONE


url = input("Enter an URL: ")

try:
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
except:
  print("Unvalid URL")
  quit()

tags = soup("img")
print("Total Images Found:", len(tags))

for tag in tags :
    link = tag.get('src')
    if link is None :
        continue
    if not link.startswith("http") :
        link = url + link
    print(link)


