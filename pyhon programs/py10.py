
### K #####

for i in range(1, 6):
    for j in range(1, 6):
        if j==1 or i+j==4 or i-j==2:
            print("*",end='  ' )
        else:
            print(" ", end=' ')
    print("")