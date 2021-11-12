import numpy as np
from functools import reduce
years = np.arange(1900, 2020+1, 1)
def intercalary(all):
    list1 = list(filter(lambda i: i % 400 == 0, all)) #list of years divisible by 400
    list2 = list(filter(lambda i: i % 400 != 0, all)) #list of years not divisible by 400
    list3=list(filter(lambda i: i % 100 != 0, list2))#list of years not divisible by 100
    list4=list(filter(lambda i: i % 4 == 0, list3)) #list of years divisible by 4
    return  list(reduce(lambda total, value: total + value, (list1,list4)))
def number_of_days(year,month,intercal) :
    year_list=[]
    year_list.append(year)
    identification=intercal(year_list) #check for a leap year
    list1=[31,28,31,30,31,30,31,31,30,31,30,31]
    list2=[31,29,31,30,31,30,31,31,30,31,30,31]
    if identification!=[]: #determining the number of days according to the year
        ans=list2[(int(month)-1)]
    else :
        ans=list1[(int(month)-1)]
    return ans
print("list of leap years")
print(intercalary(years))
import sys
help=1
while help==1: #cycle to repeat the program
 help3=1
 while help3==1 :
  try :
    print("enter the year (value must be greater than 0)")
    val_year=int(input())
    if val_year<0 :
      help3=1
      raise OverflowError
    else :
      help3=2
  except ValueError as er:
    print(er)
    print("you entered a value in the wrong format, enter an integer")
    help3=1
  except OverflowError :
    print("you entered an incorrect value")
    help3=1
 help3=1
 while help3==1 :
  try :
    print("enter the month (an integer from 1 to 12)")
    Val_month=int(input())
    if Val_month>13 or Val_month<0 :
      help3=1
      raise OverflowError
    else :
      help3=2
  except ValueError as er:
    print(er)
    print("you entered a value in the wrong format, enter an integer")
    help3=1
  except OverflowError :
    print("you entered an incorrect value")
 print(number_of_days(val_year,Val_month,intercalary))
 print("to restart the program, write 'again', and to exit anything else")
 again=input()
 if again=="again":
        hellp=1
 else:
     sys.exit()