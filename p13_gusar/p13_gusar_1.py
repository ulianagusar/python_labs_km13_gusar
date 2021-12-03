import string
file = open('gadsby.txt', 'r')
lines = file.readlines()
list_count=[]
for let in string.ascii_lowercase :#separating the letters of the alphabet
  count=0
  for line in lines:
    line.upper()
    for letter in line:
        if let==letter:
            count=count+1#accrual
  list_count.append(count)
file.close()
suma=0
for i in range(0,len(list_count)):
    suma=suma+int(list_count[i])#the sum of all letters
listforproz=[]
for i in list_count:
  proz=(int(i)/suma)*100#determination of interest
  listforproz.append(proz)
helpdict={}
for i in range(0,len(string.ascii_lowercase)):
    helpdict[string.ascii_lowercase[i]]=listforproz[i]
listforproz=sorted(listforproz,reverse=True)#sort list
ansdict={}
for i in listforproz:
    for k in helpdict.keys():
        if helpdict[k]==i:
          ansdict[k]=round(helpdict[k],3)
listkey=[]
for key_val in ansdict.keys():
    listkey.append(key_val)
for i in range(0,5):
    print(listkey[i],":",ansdict[listkey[i]],"%")
for ff in range(-5,0):
    print(listkey[i],":",ansdict[listkey[i]],"%")