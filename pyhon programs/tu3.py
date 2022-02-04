t=('abc','xy','aba','1221')
i=0
for x in t:
    if len(x)>2 and x[0]==x[-1]:
        print(x)
    i=i+1