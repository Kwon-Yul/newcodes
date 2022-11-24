n_list = [1,2,3,4,5,6,7,8,9,10]
even_list = []
for i in filter(lambda x: x%2==0, n_list):
    even_list.append(i)
    
print(even_list)

#리스트 함수를 이용하여 나타내었을 경우
even_list1 = list(filter(lambda y: y%2==0, n_list))
print(even_list1)