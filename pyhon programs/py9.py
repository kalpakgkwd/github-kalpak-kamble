
##### A #######

for i in range (1,6):
    for j in range (1,10):
        if i+j==6 or (i==3 and (j>2 and j<8) )or j-i==4 :
            print("*",end=" ")
        else :
            print(" ",end=' ')
    print("")