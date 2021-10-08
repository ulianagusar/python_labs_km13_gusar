salary_list=[6.4,9.35,11.4,14,23.8,28.15,34.7] #початкова зарплата
print("salary table")
salary2_list=[]
indexing_list=[]
for i in range(0,len(salary_list)):
    a=salary_list[i]
    salary2_list.append(round((a+a*0.3),2)) #список для збереження оновленої зарплати
    print(round((a+a*0.3),2),end=" ")
print()
for i in range(0,len(salary_list)):
    a=salary_list[i]
    indexing_list.append(round((a*0.3),2)) #список для збереження індексації
    print(round((a*0.3),2),end=" ")
