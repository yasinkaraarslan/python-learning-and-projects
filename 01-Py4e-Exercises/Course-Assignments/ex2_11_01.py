import re 

fname = input("Enter a File Name: ")

fhand = open(fname).read()

lst = list()

for line in fhand :
       line = line.rstrip()
       y = re.findall("^New Revision: ([0-9]+)", line)
       if len(y) == 0 :
              continue
       for num in y :
              num = int(num)
              lst.append(num)

print(sum(lst) / len(lst))

    





