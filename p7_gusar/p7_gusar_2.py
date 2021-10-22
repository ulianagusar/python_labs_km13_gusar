print("enter the color in RGB encoding")
help1=1
while help1==1:
    try: #checking the correctness of the input format
      val1=int(input())
      help1=2
      if ((val1 > 255)&(val1 < 0)):  #check for correctness of value
         print("The number does not belong to the coding, enter another number")
         help1 = 1
    except ValueError:
      print("Incorrect format, enter an integer")
      help1=1
help2=1
while help2==1:
    try:
      val2=int(input())
      help2=2
      if ((val2 > 255)&(val2 < 0)):
         print("The number does not belong to the coding, enter another number")
         help2 = 1
    except ValueError:
      print("Incorrect format, enter an integer")
      help2=1
help3=1
while help3==1:
    try:
      val3=int(input())
      help3=2
      if ((val3 > 255)&(val3 < 0)):
         print("The number does not belong to the coding, enter another number")
         help3 = 1
    except ValueError:
      print("Incorrect format, enter an integer")
      help1=3
print(val1,val2,val3)
list=[]
val11=val1//16
val12=int(((val1/16)-val11)*16)
val21=val2//16
val22=int(((val2/16)-val21)*16)
val31=val3//16
val32=int(((val3/16)-val31)*16)
def fun(a):  #function to reduce the size of the program
    if a  in range(0,10):
       list.append(str(a))
    elif a==10:
       list.append("A")
    elif a==11:
       list.append("B")
    elif a==12:
       list.append("C")
    elif a==13:
       list.append("D")
    elif a==14:
      list.append("E")
    elif a==15:
      list.append("F")
fun(val11)
fun(val12)
fun(val21)
fun(val22)
fun(val31)
fun(val32)
dd=''.join(list) #translate the list into a string
print("code in hexadecimal ",dd)
