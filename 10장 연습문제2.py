#f = lambda x : x*x
#f(10,10)

# 위 코드에서 10,10이 아닌 변수가 x 하나밖에 없기 때문에, 10만 넣으면 된다.
f1 = lambda x: x*x
print(f1(10))

#f = lambda x,y : x+y
#f(10)

#위 코드에서는 변수가 두개이기 때문에 x, y에 할당되는 두 개의 수를 넣어야 한다.

f2 = lambda x,y : x+y
print(f2(10,10))


#f3 = lambda x,y : z =100, x+y+z  z도 변수로 쳐야 한다.
f3 = lambda x,y,z : x+y+z
print(f3(10,20,100))