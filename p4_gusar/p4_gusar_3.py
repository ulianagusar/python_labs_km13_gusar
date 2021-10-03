dop=0 
while(dop==0):
    print("enter the duration of your conversations in minutes")
    time =int(input()) 
    if((time<=50)&(time>=0)):
       dop = 1
       print("you have to pay 100")
    elif((time>50)&(time<=100)): 
       print("you have to pay 150")
       dop = 1
    elif(time>100):
       print("you have to pay",(((time-100)*2)+150))
       dop = 1
    else:
       print("such a value is impossible,enter again")
       dop=0