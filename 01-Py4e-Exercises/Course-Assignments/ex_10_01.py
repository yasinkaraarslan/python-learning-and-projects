fname = input("Enter a File Name: ")

if len(fname) < 1 : fname = "mbox-short.txt"

try :
    fhand = open(fname)
except :
    print("File is not Found!")
    quit()    

counts = dict()

for line in fhand :
    if line.startswith("From ") :
        line =line.rstrip()
        hour = line.split()
        h = hour[5]
        exa = h[0:2]
        counts[exa] = counts.get(exa, 0) + 1 
        sorted(counts.items())
for k,v in sorted(counts.items()) :
    print(k,v)

      


        



        
