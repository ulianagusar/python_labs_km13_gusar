file_list=[]
for data in range (1880,2020):
    file_list.append("yob"+str(data)+".txt")#list of file names
list_file=[]
for file in file_list:
   file = open(file, 'r')
   lines = file.readlines()
   list_file.append(lines)
file.close()
listmen=[]
listwomen=[]
for file in list_file:
    counter1=0
    counter2=0
    ans=0
    an2=0
    for lines in file:
        if "F" in lines:
           lines=lines.split(",")
           if int(lines[2])>counter1:#determining the most commonly used female name
               counter1=int(lines[2])
               ans=lines[0]
        else:
            lines=lines.split(",")
            if int(lines[2])>counter2:#determining the most commonly used male name
               counter2=int(lines[2])
               an2=lines[0]
    listmen.append(an2)
    listwomen.append(ans)
setmen=set(listmen)
setwomen=set(listwomen)#selection of unique elements
dictres={}
for name in setmen :
    counter=0
    for name2 in listmen:
        if name==name2 :
            counter=counter+1
    dictres[name]=counter
dictres2={}
for name in setwomen :
    counter=0
    for name2 in listwomen:
        if name2==name :
            counter=counter+1#counting how many times the name became more popular
    dictres2[name]=counter
setressor=sorted(dictres.items(),key=lambda keyval : keyval[1],reverse=True)#sorting values
setres2sor=sorted(dictres2.items(),key=lambda keyval2 : keyval2[1],reverse=True)
for item1, key1 in setressor:
    print(item1, key1)
print("..............")
for item2, key2 in setres2sor:
    print(item2, key2)
