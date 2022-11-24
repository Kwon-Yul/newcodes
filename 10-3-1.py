a_list = ['a','b','c','d']
upper_a_list = []
def to_upper():
    for i in a_list:
        s = i.upper()
        upper_a_list.append(s)
        
    print(upper_a_list)

to_upper()

# lambda 함수를 이용하였을 경우
upper_a_list1 = list(map(lambda x: x.upper(),a_list))
print(upper_a_list1)
        