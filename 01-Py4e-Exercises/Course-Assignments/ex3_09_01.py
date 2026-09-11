fname = input("Enter File: ")
if len(fname) < 1 : fname = "mbox-short.txt"
try :
    fhand = open(fname)
except :
    print("File is not Found")
    quit()

counts = dict()

for line in fhand :
    if line.startswith('From ') :
        line = line.rstrip()
        mails = line.split()
        day = mails[2]
        counts[day] = counts.get(day, 0) + 1 
print(counts)

       
      
       
        


    

