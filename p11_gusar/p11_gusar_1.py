# ВАШ КОД ТУТ
def cons(head,tail=[]):
    ansver=[head]+tail #merging elements
    return ansver
# ПЕРЕВІРКА
l = cons(3, 
        cons(2, 
            cons(1,[])))
print(f'Result: {l}')
assert l == [3, 2, 1], 'Failed test 1'
assert cons(1) == [1], 'Failed test 2'
print('All tests good!')
def sum(lst):
    if lst==[] : #The base case
        return 0
    else:
        first_el=int(lst[0])
        lst.remove(lst[0])
        return first_el+sum(lst) #recursion
print(l)
#print(sum(l))
assert sum(l) == 6, 'Failed on sum'
print('All tests good!')