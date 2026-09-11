text = input("Enter Something that You Want: ")

if len(text) < 1 : text = "Hi Yasin"

counts = dict()

lst = list()

alpha = "abcdefghijklmnopqrstuvwxyz"

for line in text :
    line = line.rstrip()
    let = line.lower()
    for cha in let :
           if cha in alpha :
                   counts[cha] = counts.get(cha, 0) + 1
           
for k,v in counts.items() :
        tup = (v,k)
        lst.append(tup)

for a,b in sorted(lst, reverse=True) :
       print(a,b)


