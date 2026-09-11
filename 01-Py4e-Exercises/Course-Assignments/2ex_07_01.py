fh = input("Enter The File Name: ")
try :
    sh = open(fh)
except :
    print("File Cannot Be Opened" , fh)
    quit()
count = 0 
total = 0.0
for line in sh :
   if not line.startswith("X-DSPAM-Confidence:") :
    continue 
   colon_pos = line.find(":")
   piece = line[colon_pos + 1:]
   value = float(piece.strip())
   count = count + 1
   total = total + value
 
if count > 0 :
   average = total / count 
   print("Average spam confidence: " , average)
else :
   print("Not Found")