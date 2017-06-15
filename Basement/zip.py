a = [1,2,3]
b = [4,5,6]
print (list(zip(a,b)))
for i,j in zip(a,b):
    print (i/2,j*2)

list1 = [1,2,3,4,5]
squaredList = list(map(lambda x: x*x, list1))
print(squaredList)
