import sys
help=1
while help==1: #cycle to repeat the program
 try:
  print("enter coefficients of quadratic equation")
  print("enter a")
  a=int(input())
  print("enter b")
  b=int(input())
  print("enter c")
  c=int(input())
  dis=b*b-4*a*c #calculating the discriminant
  if dis<0: #check for a negative value under the root and whether there are roots in the equation
     raise ValueError
  val1=((0-b+pow(dis,1/2))/(2*a))#finding roots
  val2=((0-b-pow(dis,1/2))/(2*a))
  if(val2==val1): #option when the equation has one root
     print(val1)
     print("the equation has one root")
  print(val1)
  print(val2)
 except ZeroDivisionError as e:
    print(e)
    print("you probably entered a linear equation")
 except OverflowError as e:
    print(e)
    print("the result is too large")
 except ValueError as e:
    print(e)
    print("the equation has no roots or you entered the value in the wrong format")
 finally:
    print("to restart the program, write 'again', and to exit anything else")
    again=input()
    if again=="again":
        hellp=1
    else:
     sys.exit()
