def computepay(hours, rate) :
    # print("In commputepay" , hours , rate)
    if hours > 40 :
      reg = rate * hours
      otp = (hours - 40.0) * (rate * 0.5)
      pay = reg + otp
    else :
        pay = hours * rate 
    return pay 
      
    
hours = input('Enter Hours: ')
rate = input('Enter Rate: ')
try:
    fh = float(hours)
    fr = float(rate)
except:
    print("Error,please enter numberic input")
    quit()
xp = computepay(fh,fr )

print("Pay:" ,xp)