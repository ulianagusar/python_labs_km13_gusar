salary_list=[6.4,9.35,11.4,14,23.8,28.15,34.7] #initial salary
print("salary table")
def salary_val(val1):
    return round((val1+val1*0.3),2) #calculation of a new salary
def indexing_val (val2):
    return round((val2*0.3),2)#indexing calculation
def indexing (val2): #carring
    return list(map(val2, salary_list))
print(indexing(salary_val))
print(indexing(indexing_val))