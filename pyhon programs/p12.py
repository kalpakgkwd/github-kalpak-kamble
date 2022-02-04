
## Y ##

for i in range(1, 6):
    for j in range(1, 6):
        if (i+j==6 and j>3) or (i==j and j<4) or (j==3 and i>2) :
            print("*",end=' ' )
        else:
            print(" ", end=' ')
    print("")