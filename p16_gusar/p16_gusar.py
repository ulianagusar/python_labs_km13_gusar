def decorator(active=False):
    def wrap(func):
        def wrapper(*args):
            if active:
                newlist2=[]
                list11=func(*args) 
                for i in list11:
                    newlist=[]
                    while i!=[]:
                      nn=tuple(i[0:4])
                      del i[0:4]
                      newlist.append(nn)
                    newlist2.append(newlist)
                return newlist2
            else:
               return func(*args)
        return wrapper
    return wrap
h2=1
while h2==1:#check
    try:
        print("Enter True if you want to sort the list, otherwise False")
        sort=input()
        if sort=="False":
            sort_bool=False
        elif sort=="True":
            sort_bool=True
        else:
            raise OverflowError
        h2=2
    except OverflowError:
        print("you only need to enter True or False")
        h2=1
@decorator(sort_bool)
def list_in_list(a):
    n=int(a/16)
    list_for_ans=[]
    for i in range(1,n+1):
        nn=i*16
        list_for_ans2=[]
        list1=[b for b in range(nn-15,nn-7)]
        list2=[c for c in range(nn-8,nn)]
        list_for_ans2.append(nn)
        while (list1!=[]):
            list_for_ans2.append(list1[0])
            list_for_ans2.append(list1[1])
            del(list1[0])
            del(list1[0])
            if list2 !=[]:
             list_for_ans2.append(list2[-1])
             list_for_ans2.append(list2[-2])
             del(list2[-1])
             del(list2[-1])
        del(list_for_ans2[-1])
        list_for_ans.append(list_for_ans2)
    return list_for_ans
h=1
while h==1:#check
    try:
        print("enter the number of pages,the number must be a multiple of 16")
        pages=int(input())
        if pages<16 or a>1280:
            raise ZeroDivisionError
        if pages%16!=0:
            raise OverflowError
        h=2
    except ValueError:
        print("value must be an integer")
        h=1
    except ZeroDivisionError:
        print("the book must contain at least 1 notebook and be less than 1280 pages")
        h=1
    except OverflowError:
        print("the book must contain a multiple of 16")
        h=1
res=list_in_list(pages)
print("In a notebook 16 sheets")
for i in res:#scan the list
    if type(i[0])!=tuple:
        print(i) 
    else:
        for g in i:
            print(g)