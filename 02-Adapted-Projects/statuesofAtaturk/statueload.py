import urllib.request, urllib.parse, urllib.error
import http
import sqlite3
import json 
import time
import ssl 
import sys 

serviceurl = 'https://py4e-data.dr-chuck.net/opengeo?'

conn = sqlite3.connect('statues.sqlite')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Locations')

cur.execute('''
CREATE TABLE IF NOT EXISTS Locations (adress TEXT, statuedata TEXT)''')

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

fh = open('statue.data')
count = 0 
nofound = 0 
for line in fh :
    if count > 10 :
        print('Retrieved 10 Locations, restart to retrieve more')
        break
    adress = line.strip()
    print('')
    cur.execute("SELECT statuedata FROM Locations WHERE adress = ?",
        (memoryview(adress.encode()), ))

    try:
        data = cur.fetchone()[0]
        print("Found in database", adress)
        continue
    except:
        pass

    if 'ataturk' in adress.lower() or 'atatürk' in adress.lower():
        adress = "Atatürk - " + adress

    parms = dict()
    parms['q'] = adress

    url = serviceurl + urllib.parse.urlencode(parms)

    print('Retrieving', url)
    uh = urllib.request.urlopen(url, context=ctx)
    data = uh.read().decode()
    print('Retrieved', len(data),'characters',data[:20].replace('\n',' '))
    count = count + 1 

    try: 
        js = json.loads(data)
    except:
        print(data)
        continue 

    if not js or 'features' not in js:
        print('==== Download Error ====')
        print(data)
        break

    if len(js['features']) == 0:
        print('==== Object not found ====')
        nofound = nofound + 1

    cur.execute('''INSERT INTO Locations (adress, statuedata)
        VALUES ( ?, ? )''',
        (memoryview(adress.encode()), memoryview(data.encode()) ) )

    conn.commit()

    if count % 10 == 0 :
        print('Pausing for a bit...')
        time.sleep(5)

if nofound > 0 :
    print('Number of features for which the location could not be found', nofound)

print('Run statuedump.py to read the data from the database so you can visualize it on a map.')