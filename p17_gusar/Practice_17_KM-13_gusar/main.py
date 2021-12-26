import sys

from exp_root.exponentation import exp2 ,exp3
from exp_root.root import root2 ,root3
from factorial.factorial import fact
from logarithm.logarithm import log, lg ,ln

def main():
    help=1
    while help==1:
         print("Choose function\n 1-factorial\n 2-exponentation2\n 3-exponentation3\n 4-root2\n 5-root3\n 6-log\n 7-ln\n 8-lg")
         help2=1
         while help2==1:
          try:
             print("enter the function number")
             number=int(input())
             if number>8 or number<1:
                 raise ZeroDivisionError
             help2=2
          except ValueError:
             print("you cannot enter a value other than a number")
             help2=1
          except ZeroDivisionError:
             print("you must enter a number from 1 to 8")
             help2=1
         if number==1:
            print("enter a value")
            help3=1
            while help3==1:
             try:
                znach=int(input())
                help3=2
             except ValueError :
                print("you must enter an integer")
                help3=1
            print("Result",fact(znach))
         elif number==2:
             print("enter a value")
             help3 = 1
             while help3 == 1:
                 try:
                     znach = float(input())
                     help3 = 2
                 except ValueError:
                     print("you cannot enter a value other than a number")
                     help3 = 1
             print("Result", exp2(znach))
         elif number==3:
             print("enter a value")
             help3 = 1
             while help3 == 1:
                 try:
                     znach = float(input())
                     help3 = 2
                 except ValueError:
                     print("you cannot enter a value other than a number")
                     help3 = 1
             print("Result", exp3(znach))
         elif number==4:
             print("enter a value")
             help3 = 1
             while help3 == 1:
                 try:
                     znach = float(input())
                     if znach<0:
                         raise ZeroDivisionError
                     help3 = 2
                 except ValueError:
                     print("you cannot enter a value other than a number")
                     help3 = 1
                 except ZeroDivisionError:
                     print("you have entered an invalid value")
                     help3 = 1
             print("Result", root2(znach))
         elif number==5:
             print("enter a value")
             help3 = 1
             while help3 == 1:
                 try:
                     znach = float(input())
                     help3 = 2
                 except ValueError:
                     print("you cannot enter a value other than a number")
                     help3 = 1
                 except ZeroDivisionError:
                     print("you have entered an invalid value")
                     help3 = 1
             print("Result", root3(znach))
         elif number==6:
             print("enter the base")
             help3 = 1
             while help3 == 1:
                 try:
                     znach = float(input())
                     if znach<0 or znach==1:
                         raise ZeroDivisionError
                     help3 = 2
                 except ValueError:
                     print("you cannot enter a value other than a number")
                     help3 = 1
                 except ZeroDivisionError:
                     print("you have entered an invalid value")
                     help3 = 1
             print("enter a value")
             help4 = 1
             while help4 == 1:
                 try:
                     znach2 = float(input())
                     help4 = 2
                     if znach2<0:
                         raise  ZeroDivisionError
                 except ValueError:
                     print("you cannot enter a value other than a number")
                     help4 = 1
                 except ZeroDivisionError:
                     print("you have entered an invalid value")
                     help4 = 1
             print("Result", log(znach,znach2))
         elif number==7:
             print("enter a value")
             help3 = 1
             while help3 == 1:
                 try:
                     znach = float(input())
                     if znach<0:
                         raise ZeroDivisionError
                     help3 = 2
                 except ValueError:
                     print("you cannot enter a value other than a number")
                     help3 = 1
                 except ZeroDivisionError:
                     print("you have entered an invalid value")
                     help3 = 1
             print("Result", ln(znach))
         elif number==8:
             print("enter a value")
             help3 = 1
             while help3 == 1:
                 try:
                     znach = float(input())
                     if znach<0:
                         raise ZeroDivisionError
                     help3 = 2
                 except ValueError:
                     print("you cannot enter a value other than a number")
                     help3 = 1
                 except ZeroDivisionError:
                     print("you have entered an invalid value")
                     help3 = 1
             print("Result", lg(znach))
         print("to restart the program write 'again'")
         ans=input()
         if ans=="again":
             help=1
         else:
             sys.exit()






if __name__ == '__main__':
    main()


