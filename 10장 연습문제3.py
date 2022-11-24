# 10장의 6번 연습문제입니다.
n_list = [44,66,34,24,144,98,38,568,234,345]
new_list = []
for i in n_list:
    if i%12 ==0:
        new_list.append(i)
        
print(new_list)

#filter 함수를 사용하여 나타내면 다음과 같습니다.
new_list1 = list(filter(lambda x: x%12==0,n_list))
print(new_list1)

#list 축약 표현을 사용하면 다음과 같습니다.
new_list2 = [x for x in n_list if x %12== 0]
print(new_list2)