#연습문제 10번입니다.
n_list = list(range(1,101))
new_list=[]
b = []
for i in n_list:
    if i % 6 == 0 and i % 7 == 0:
        new_list.append(i)
        
print(new_list)

#filter 함수와 람다 함수를 사용하면 다음과 같습니다.
for i in filter(lambda x: x%6==0 and x%7==0,n_list):
    b.append(i)
    
print(b)

#리스트 축약 표현을 사용하면 다음과 같습니다.
c = [x for x in n_list if x%6==0 and x%7==0]
print(c)