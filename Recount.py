canditates=[]
name=[]
counter=[]
for i in range(10000):
    names=input()
    if(names=='***'):
        break
    canditates.append(names)
name=set(canditates)
for j in name:
    count1=0
    for k in canditates:
        if(j==k):
            count1=count1+1
    counter.append(count1)
name=list(name)
winner=max(counter)
index1=counter.index(winner)
count2=counter.count(winner)
if(count2>1):
    print('Runoff!')
else:   
    print(name[index1])
