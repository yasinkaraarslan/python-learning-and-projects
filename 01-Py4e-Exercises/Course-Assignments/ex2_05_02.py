lst = list()
while True :
    num = input("Enter a Number: ")
    if num == 'done' :
        break
    try :
        fnum = float(num)
    except :
        print("Please Enter A Numberic İnput")
        continue 
    lst.append(fnum)

# print(lst)

print(max(lst))
print(min(lst))