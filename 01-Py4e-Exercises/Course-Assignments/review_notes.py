# NOTES : FILE  HANDLİNG and STRING SLICING

# continue : Skips the current ,iteration of the loop , jumps to the next line immediately.

# find(":") : Finds the index (numerical position) of the colon character.

# [pos+1:] : Slices the string from the character right after the colon until the very end

count = 0
total = 0.0

fname = input("Enter a File name: ")

fhand = open(fname)

for line in fhand :
    # VIP Filter : Skip irrelevant lines and guard the code below
    if not line.startswith("X-DSPAM-Confidence:"):
        continue 
    colon_pos = line.find(":")
    piece = line[colon_pos + 1:]
    value = float(piece.strip()) # Convert

    count = count + 1 
    total = total + value 

# LISTS VS STRINGS

# Lists are mutable (we can change their elements using indexes)

# but strings are immutable (we cannot change individual characters) 


han = open('mbox-short.txt')

for line in han :
    line = line.rstrip()
    wds = line.split()

    # guardian in compund system

    if len(wds) < 3 or wds[0] != 'From' :
        continue 
    print(wds[2])

#   QUICK DEBUG and GUARDIAN NOTES 

# THE PROBLEM :
# Empty lines -> split() creates empty list [] -< causes index error

# THE SOLUTION :

# Check list length before accessing an index

# THE TRICK :

# In 'or' statements, if the left side is True , Pyhton ignores the Right side

# SAFE CODE:

# if len(wds) < 3 or wds[0] != 'From' : continue

# print(wds[2])

# domain name (instead of the address) where the message was sent from instead of who the mail came from (i.e., the whole email address)


d = {'a':10, 'c':22, 'b':1}
tmp = list()

# 1.Swap to (value,key) to sort by values.
for k, v in d.items() :
    tmp.append( (v, k) )
# print(tmp)

# 2.Sort the list dencending (largest to smallest) using reverse=True
tmp = sorted(tmp, reverse=True)
# print(tmp)

# List comprehension :  A shorthand way to create a list in a single line

c = {'a':10, 'b':1, 'c':22}
print(sorted( [ (v, k) for k, v in c.items() ] ) )

#1.Loop through dict items
#2.Swap them to (v,k) and put inside []
#3.Sort the final list 

# l. append() accepts exactly one item. lst.append( (v,k) ) or tup = (v,k) lst.append(tup)

# 2.  Move the final code block to the far left so it runs only once after the loop finishes completely.

# 3. The items() method in Python returns a view object that displays a list of a given dictionary's key-value tuple pairs. It allows you to loop through both the keys and the values simultaneously in a clean and efficient way

# Standard division (/) : Always returns a float, ven if the result is a whole number.

# Integer Division (//) : Divides and rounds down to the nearest whole number , dropping the decimal part completely

