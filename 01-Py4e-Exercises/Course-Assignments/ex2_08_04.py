fname = input("Enter a File Name: ")

mail = open(fname)

count = 0

for line in mail :
    if line.startswith("From ") :
        words = line.split()
        count = count + 1
        print(words[1])
print("There Were" , count , "lines in the file with From as the first word")
   