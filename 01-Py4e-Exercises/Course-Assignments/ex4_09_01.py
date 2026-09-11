fname = input("Enter A File Name: ")

if len(fname) < 1 : fname = "mbox-short.txt"

try :
    fhand = open(fname)
except :
    print("File is not Found")
    quit()

counts = dict()

mpt = list()

for line in fhand :
    if line.startswith("From ") :
        line = line.rstrip()
        mails = line.split()
        pers = mails[1]
        counts[pers] = counts.get(pers, 0) + 1
        for k,v in counts.items() :
            tup = (v,k)
            mpt.append(tup)

mst = sorted(mpt, reverse=True)

for v,k in mst[:1] :
    print(k,v)


           

    
    
#bigpers = None
#bigcount = None 
#for per,count in counts.items() :
    #if bigcount is None or count > bigcount :
      #  bigcount = count 
       # bigpers = per
# print(bigpers, bigcount) 

