mylist=[10,20,30]
print(mylist)

mylist.append(40)
mylist.append('abc')
mylist.append([1,2,3])
print(mylist)

mylist.extend([4,5,6])
print(mylist)

mylist.append(10)
print(mylist)
mylist.remove(10)
print(mylist)

mylist.append(10)
print(mylist)
for x in mylist:
    if x==10:
        mylist.remove(10)
print(mylist)


x=mylist.pop(2)
print(x)
print(mylist)

mylist.insert(4,30)
mylist.insert(7,30)
print(mylist)
x=mylist.count(30)
print(x)

mylist.reverse()
print(mylist)
















