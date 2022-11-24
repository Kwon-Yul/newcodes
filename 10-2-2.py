n_list = [1,2,3,4,5,6,7,8,9,10]
odd_list = []
for i in filter(lambda x: x%2==1, n_list):
    odd_list.append(i)
    
print(odd_list)

#리스트 함수를 사용하여 나타냈을 경우
odd_list1 = list(filter(lambda y: y%2==1,n_list))
print(odd_list1)