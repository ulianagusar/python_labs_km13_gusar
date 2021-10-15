help1=1 # допоміжна знінна
while help1==1: # цикл для повтору програми
   print("enter the first sentence")
   first = input()
   print("enter the second sentence")
   second = input()
   first = first.lower() #переведення літер в нижній регістр
   second = second.lower()
   set1 = set()
   set2 = set()
   for i in first:
       if i.isalpha() == True: #відділення літер
           set1.add(i)
   for i in second:
       if i.isalpha() == True:
           set2.add(i)
   if set2.issubset(set1) == True:# перевірка чи входять усі літери з другого речення в перше
       print("the first sentence :", set1)
       print("the second sentence:", set2)
       print("from the letters of the first sentence you can make a second sentence")
   else:
       print("the first sentence :", set1)
       print("the second sentence:", set2)
       print("from the letters of the first sentence it is impossible to make the second sentence")
   print("to repeat the program, write : again , to exit anything else ")
   repeat=input()
   if (repeat=="again"):
       help1=1
   else:
    exit()