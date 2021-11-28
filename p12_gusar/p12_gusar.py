dirs = [
    ( 'folder1',
        [
            'file1',
            ( 'folder2', 
                [
                    'file2',
                    'file3'
                ] 
            ),
            ( 'folder3', 
                [
                    'file3', 
                    'file4',
                    ('folder4', ['file3'])
                ] 
            ),
            'file5'
        ]
    )
]

# ВАШ КОД ТУТ
def search(dirts,filename,text="",list_ans=[]):
    if (type(dirts)==list or type(dirts)==tuple) and (type(dirts[i])!=list and type(dirts[i])!=tuple for i in range(0,len(dirts)) ) and (filename in dirts):
        if text==None:
              list_ans=[] 
        text=text+"/"+filename
        list_ans.append(text)#adding an answer to the list
    #check if there is a folder in the folder with the searched file
    if (type(dirts)==list or type(dirts)==tuple) and (type(dirts[i])==list or type(dirts[i])==tuple for i in range(0,len(dirts)) ) and (filename in dirts):
      for s in dirts :
         if type(s)==list or type(s)==tuple :
                search(s,filename,text,list_ans)
    elif  type(dirts)==list :
      for s in dirts :
        if type(s)==list or type(s)==tuple :
               search(s,filename,text,list_ans)
      return list_ans
    elif type(dirts)==tuple :
            if list_ans==None:
              list_ans=[]  
            text=text+"/"+(dirts[0]) #add path to file
            search(dirts[1],filename,text,list_ans)    
#Програма працює,якщо робити 1 print за раз
# ПЕРЕВІРКА

print(search(dirs, 'file1'))
print(search(dirs, 'file2'))
print(search(dirs, 'file3'))
print(search(dirs, 'file4'))
print(search(dirs, 'file5'))
print(search(dirs, 'file6'))
print(search(dirs, 'folder1'))

assert search(dirs, 'file1') == ['/folder1/file1'], 'Failed test for file1'
assert search(dirs, 'file2') == ['/folder1//folder2/file2'], 'Failed test for file2'
assert search(dirs, 'file3') == ['/folder1//folder2/file3', '/folder1//folder3/file3', '/folder1//folder3//folder4/file3'], 'Failed test for file3'
assert search(dirs, 'file4') == ['/folder1//folder3/file4'], 'Failed test for file4'
assert search(dirs, 'file5') == ['/folder1/file5'], 'Failed test for file5'
assert search(dirs, 'file6') == [], 'Failed test for file6'
assert search(dirs, 'folder1') == [], 'Failed test for folder1'
print('All tests good!')