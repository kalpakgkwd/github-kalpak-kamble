mylist=[8,2,4,5,6,1,9]
for i in range (len(mylist)-1):
    for j in range(len(mylist)-1):
        if mylist[j]>mylist[j+1]:
            t=mylist[j]
            mylist[j]=mylist[j+1]
            mylist[j+1]=t
            print(mylist)
print(mylist)

