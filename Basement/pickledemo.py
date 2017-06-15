import pickle

a = {'a':111,2:[23,1,4],'23':{1:2,'d':'sad'}}
file = open('test.pickle','wb')
pickle.dump(a,file)
file.close()

# with 的好处在于不用人为的进行close file操作
with open('test.pickle','rb') as file:
# file = open('test.pickle','rb')
    b = pickle.load(file)
    # file.close()
    print(b)