import itertools
help=1
while help==1:#check values
  try:
    row=int(input())
    if row<0:
        raise ZeroDivisionError
    help=2
  except ValueError:
    print("You have entered an incorrect value")
    help=1
  except ZeroDivisionError:
    print("Value must be a positive integer")
    help=1
def pascal():
    row = 0
    while True:
        str_for_ans=""
        for i in range(0,row+1):
         str_for_ans=str_for_ans+" "+str(len(list(itertools.combinations(range(0,row),i))))#creating strings with combinations
        yield str_for_ans
        row=row+1
res = pascal()
for i in range(0,row+1):
   print(next(res))