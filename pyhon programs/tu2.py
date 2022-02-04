mylist=[(2,5),(1,2),(4,4),(2,3),(2,1)]
print(mylist)
for i in range(len(mylist)-1):
    for j in range(len(mylist)-1):
        if mylist[j][1]>mylist[j+1][1]:
            t=mylist[j]
            mylist[j]=mylist[j+1]
            mylist[j+1]=t

print(mylist)