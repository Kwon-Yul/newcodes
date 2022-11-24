n_list = [10,20,30]
twicelist = []
triplelist = []
def twice():
    for i in n_list:
        s = i *2
        twicelist.append(s)
        
    print(twicelist)
    
def triple():
    for x in n_list:
        y = x*3
        triplelist.append(y)
        
    print(triplelist)
    
    
twice()
triple()

#lambda 함수를 이용하였을 경우

twicelist1 = list(map(lambda x: x*2,n_list))
triplelist1 = list(map(lambda y: y*3,n_list))

print(twicelist1)
print(triplelist1)