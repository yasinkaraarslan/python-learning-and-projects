import sqlite3

con = sqlite3.connect("domain.sqlite")
cur = con.cursor()

cur.execute("DROP TABLE IF EXISTS DomainCount")

cur.execute("CREATE TABLE DomainCount (domain TEXT , count INTEGER)")

fname = input("Enter a File Name: ")

if len((fname)) < 1 : fname = "mbox-short.txt"
fh = open(fname)
for line in fh :
     
    if not line.startswith("From: ") :  continue 
    pieces = line.split()
    dom = pieces[1]
    dome = dom.split("@")
    domain = dome[1]
    cur.execute("SELECT count FROM DomainCount WHERE domain = ?", (domain,))
    row = cur.fetchone()
    if row is None :
          cur.execute("INSERT INTO DomainCount (domain,count) VALUES (?, 1)", (domain,))
    else :
         cur.execute("UPDATE DomainCount SET count = count + 1 WHERE domain = ?", (domain,))

    con.commit()

sqlstr = "SELECT domain, count FROM DomainCount ORDER BY count DESC LIMIT 5"

for row in cur.execute(sqlstr) :
     print(str(row[0]), (row[1]))

cur.close()

        
  