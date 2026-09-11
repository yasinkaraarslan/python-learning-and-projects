num = 0
tot = 0.0
while True :
    sval = input("Enter a number: ")
    if sval == "done" :
        break
    try :   
        fval = float(sval)
    except :
        print("Please Enter a Numberic input")
        continue
    
    print(fval)
    num = num + 1 
    tot = tot + fval 
    
if num > 0 :
    print(tot, num, tot/num)
    


       
    
