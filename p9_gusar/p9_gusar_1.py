import numpy as np
import itertools
def random_matrix(dim):
    """
    The function generates dim x dim array of integers
    between 0 and 10.
    """
    matrix = np.random.randint(10, size = (dim, dim))
    print(matrix)
    return matrix
def permutatiom_list(val):
  """
  the function creates a list of permutations
  """
  ans=""
  for i in range (1,val+1):
   ans=ans+str(i)
  list11 = list(itertools.permutations(ans,val))
  return list11
def product (list1,list2):
 """
 the function finds the product of the rows of the matrix
 """
 listans=[]
 help=1
 for index1 in range(0,len(list2)):
   help=1
   for index2 in range(0,len(list2[index1])):
      ans=(list1[((index2+1)*10+int(list2[index1][index2]))])*help 
      help=ans
   listans.append(ans)
   ans=1
 return listans
def dict_for_sum (d) :
 """
 the function creates a dictionary that is needed to determine the product
 """
 dict1={}
 for i in range (0,len(d)):
  for g in range (0,len(d[i])):
   dict1[((i+1)*10)+(g+1)]=d[i][g]#assigning to each element of the matrix the value of its row and column
 return dict1
def hhhh(list_permutation):
 """
 the function finds the inversion
 """
 listans=[]
 for permutatiom_str in range (0,len(list_permutation)):
  list_permutation_str=list(list_permutation[permutatiom_str])
  kut = 0
  for i in range (0,len(list_permutation_str)-1): #ordering elements
     for s in range(0,(len(list_permutation_str)-1-i)):
        if list_permutation_str[s]> list_permutation_str[s+1]:
          list_permutation_str[s], list_permutation_str[s+1]=list_permutation_str[s+1], list_permutation_str[s]
          kut+=1 #counting the number of permutations
  listans.append(kut)
 return listans
def fjf(list_inversia,list_suma) :
 """
 the function determines the sign of the terms and finds the sum
 """
 helpp=0
 list12=[]
 for i in list_inversia:
   if i==0 or i%2==0 :
     list12.append(1)
   else:
      list12.append(-1)
 for i in range(0,len(list12)) :
    ansver=list12[i]*list_suma[i]+helpp #multiplying the product of rows by -1 or 1 and finding the total amount
    helpp=ansver
 return ansver
import sys
help=1
while help==1: #cycle to repeat the program
 print("Enter the size of the matrix")
 help3=1
 while help3==1 :
  try :
    a=int(input())
    if a>10 or a<0 :
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
 print ("determinant =",(fjf(hhhh(permutatiom_list(a)),product(dict_for_sum(random_matrix(a)),permutatiom_list(a)))))
 print("to restart the program, write 'again', and to exit anything else")
 again=input()
 if again=="again":
        hellp=1
 else:
     sys.exit()