import collections
map,nums= {},collections.defaultdict(int)

def createIndex(filePath):
    with open(filePath) as reader:
        for line in reader:
            sarray=line.strip('\n').split(' ')
            for s in sarray:
                list = []
                if s not in map:
                    list.append(filePath)
                    map[s]=list
                else:
                    list = map[s]
                    if filePath not in map[s]:
                        list.append(filePath)
                nums[s]+=1

for i in range(1,4):
    createIndex("C:\\Users\\Administrator\\Desktop\\"+str(i)+".txt")

for i in map:
    print("{key}:{value}".format(key=i,value=map[i]))
for j in nums:
    print("{key}:{value}".format(key=j,value=nums[j]))
