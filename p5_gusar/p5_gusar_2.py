help1=1 # допоміжна знінна
while help1==1: # цикл для повтору програми
   print("enter the elements of the sequence, then write go")
   element=1
   list1=[] #створення пустого списку
   while(element!="go"):# введення елементыв до стоп-слова
    element=input() #Введення елементу
    list1.append(element)#додавання елементу до списку
   list1.remove('go')# виделення стоп-слова із списку
   if (len(list1)>2):
         for i in range(0,len(list1)-2): # виведення елементів списку окрім 2 останніх
            print(list1[i],",",end=" ")
         print(list1[-2],"and",list1[-1]) #виведення 2 останніх із словом and
   elif(len(list1)==2):
         print(list1[-2], "and", list1[-1])
   elif(len(list1)==1):
         print(list1[-1])
   print("to repeat the program, write : again , to exit anything else ")
   repeat=input()
   if (repeat=="again"):
       help1=1
   else:
    exit()