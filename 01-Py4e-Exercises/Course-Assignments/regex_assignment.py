import re

fh = open('regex_sum_2457283.txt').readlines()

lst = list()

count = 0

for line in fh :
    line = line.rstrip()
    x = re.findall('[0-9]+', line)
    if len(x) < 1 :
        continue 
    for n in x :
        intnum = int(n)
        lst.append(intnum)

print("Values", len(lst))
print("Total", sum(lst))
       

   

