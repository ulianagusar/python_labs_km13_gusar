# ВАШ КОД ТУТ
def rrange(begin,end,step=1):
  def rrange_main(begin,end,step):
     if begin == end: #The base case
        return []   
     elif ((step<0) and (begin<end)) or ((begin>end) and (step>0)) or step==0 :#check for correctness of value
        ansver_list=[]
        return ansver_list
     else:
         begin2=begin+step
         return [begin]+[rrange_main(begin2,end,step)]# The recursive call
  def norm_list(ansver_list) :# function to normalize the list
     ansver_list2=[]
     while(len(ansver_list)==2):
       ansver_list2.append(ansver_list[0])
       ansver_list=ansver_list[1]
     return ansver_list2
  return norm_list(rrange_main(begin,end,step))
# ПЕРЕВІРКА

x = rrange(1, 10)
y = rrange(10, 1, -1)
z = rrange(10, 1, 1)
print(x, y, z)

assert x == list(range(1, 10)), 'Failed test for simple range'
assert y == list(range(10, 1, -1)), 'Failed test for reverse range'
assert z == list(range(10, 1, 1)), 'Failed test for empty range'
print('All tests good!')