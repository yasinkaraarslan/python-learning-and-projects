
numbers = list()


while True :
    fnumb = input("Enter a Number: ")
    if fnumb == "done" :
        break
    try :
        hnumb = float(fnumb)
    except :
        print("Please Enter a numeric input")
        continue
    numbers.append(hnumb)
print(max(numbers))
print(min(numbers))

