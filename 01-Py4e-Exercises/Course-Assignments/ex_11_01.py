import re 


reg = input("Enter a Regular Expression: ")


fhand = open("mbox.txt")

count = 0

for line in fhand :
    line = line.rstrip()
    if re.search(reg, line) :
        count = count + 1
print("mbox.txt had", count , "lines that matched" , reg)

          