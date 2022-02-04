######  name ####


### K #####

for i in range(1, 6):
    for j in range(1, 6):
        if j==1 or i+j==4 or i-j==2:
            print("*",end='  ' )
        else:
            print(" ", end=' ')
    print("")

##### A #######

for i in range (1,6):
    for j in range (1,10):
        if i+j==6 or (i==3 and (j>2 and j<8) )or j-i==4 :
            print("*",end=" ")
        else :
            print(" ",end=' ')
    print("")


#####   L   #####

for i in range (1,6):
    for j in range (1,4):
        if j==1:
            print("*",end=" ")
        if i==5 :
            print("*",end=" ")
        else :
            print(" ",end=' ')
    print("")


### P ###

for i in range(1, 6):
    for j in range(1, 6):
        if j==1 or i==1 or (j==5 and i<4) or i==3 :
            print("*",end=' ' )
        else:
            print(" ", end=' ')
    print("")

##### A #######

for i in range (1,6):
    for j in range (1,10):
        if i+j==6 or (i==3 and (j>2 and j<8) )or j-i==4 :
            print("*",end=" ")
        else :
            print(" ",end=' ')
    print("")


### K #####

for i in range(1, 6):
    for j in range(1, 6):
        if j==1 or i+j==4 or i-j==2:
            print("*",end='  ' )
        else:
            print(" ", end=' ')
    print("")
