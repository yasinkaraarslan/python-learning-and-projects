day = 0
tot = 0.0
day1 = 0
while  True :
    tday = input("Enter Tempature: ")
    if tday == "off" :
        break
    try :
        sday = float(tday)
    except :
        print("Invalid Tempature")
        continue
    
    day = day + 1
    tot = tot + sday
    
    if sday < 0 :
        day1 = day1 +1
print(day)
print(tot / day)
print(day1) 