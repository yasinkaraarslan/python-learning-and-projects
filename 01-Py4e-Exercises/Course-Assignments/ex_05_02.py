maximum = None 
minimum = None 

while True :
    num = input("Enter a Number: ")
    if num == 'done' :
        break
    try :
        fnum = float(num)
    except :
        print("Please Enter A Numberic İnput")
        continue 

    if maximum is None :
      maximum = fnum 
    elif fnum > maximum :
        maximum = fnum
    if minimum is None :
       minimum = fnum
    elif fnum < minimum :
        minimum = fnum

print(maximum)
print(minimum)