# 연습문제 7번입니다.
n_list = [-22.3,29.44,902.2,45.7,-887.1,-56.3]
new_list = []
for i in n_list:
    if i>0:
        a = int(i)
        new_list.append(a)
        
print(new_list)

# filter, map, 람다 함수를 사용하면 다음과 같습니다.
a = []
for i in filter(lambda x: x>0,n_list):
    a.append(int(i))
    
print(a)

# 리스트 축약 형태로 표현하면 다음과 같습니다.
b = [int(x) for x in n_list if x>0]
print(b)
               