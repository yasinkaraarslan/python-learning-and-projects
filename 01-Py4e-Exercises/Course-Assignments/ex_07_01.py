fh = input("Enter The File Name: ")
if fh == "na na boo boo" :
    print("NA NA BOO BOO TO YOU - YOU HAVE BEEN PUNK :D")
    quit()
try :
    sh = open(fh)
except :
    print("File cannot be opened" , fh)
    quit()

count = 0

for line in sh :
    if line.startswith("Subject:") :
        count= count + 1
print("There Were" , count , "Subject Lines in" , fh)