
# print A
for row in range(7):
    for col in range(5):
        if(row==0) and (col in {1,2,3}):
            print("*",end=" ")
        elif(row in {1,2,3,4,5,6}) and (col in (0,4)):
            print("*", end=" ")
        elif row ==3:
            print("*",end=" ")
        else:
            print(" ", end=" ")
    print()

print("\n")

# print B
str = ""
for row in range(0,7):
    for col in range(0,8):
        if(col==1 or ((row==0 or row==3 or row==6) and (col<5 and col>1))or (col == 7  and (row!=0 and row!=3 and row!=6 ))):
            str = str+"* "
        else:
            str = str+" "
    str = str+"\n"
print(str)

print("\n")

# print C
str = ""
for row in range(0,7):
    for col in range(0,8):
        if((col==1 and ((row!=0 or row!=6)) or ((row==0 or row==6) and (col<5 and col>1)) or (col == 7  and (row==1 or row==5 )))):
            str = str+"* "
        else:
            str = str+" "
    str = str+"\n"
print(str)

print("\n")

#print D
str = ""
for row in range(0,7):
    for col in range(0,8):
        if(col==1 or ((row==0 or row==6) and (col<5 and col>1))or (col == 7 and (row!=0 and row!=6 ))):
            str = str+"* "
        else:
            str = str+" "
    str = str+"\n"
print(str)

print("\n")

# print E
str = ""
for row in range(0,7):
    for col in range(0,8):
        if(col==1 or ((row==0 or row==3 or row==6) and (col<6 and col>1))):
            str = str+"* "
        else:
            str = str+" "
    str = str+"\n"
print(str)

print("\n")

# print F
str = ""
for row in range(0,7):
    for col in range(0,8):
        if(col==1 or ((row==0 or row==3 ) and (col<6 and col>1))):
            str = str+"* "
        else:
            str = str+" "
    str = str+"\n"
print(str)

print("\n")


# print G
str = ""
for row in range(7):
    for col in range(8):
        if((col ==1 and row!=0 and row!=6) or((row==0 or row==6) and col>1 and col<5) or (row==3 and col<6 and col>2) or (col==7 and row!=0 and row !=2 and row!=6 and row != 3)):
            str = str+"* "
        else:
            str = str+" "
    str = str+"\n"
print(str)

print("\n")

# print H
str = ""
for row in range(7):
    for col in range(8):
        if((col ==1 or col == 6 and row!=3) or (row == 3 and col<5 and col>1 )):
            str = str+"* "
        else:
            str = str+" "
    str = str+"\n"
print(str)

print("\n")

# print I
str = ""
for row in range(7):
    for col in range(5):
        if((row ==1 or row == 6 ) or (col == 4 and row<6 and row>1 )):
            str = str+"* "
        else:
            str = str+" "
    str = str+"\n"
print(str)

print("\n")

# print J
str = ""
for row in range(10):
    for col in range(7):
        if((row ==1 ) or (col == 6 and row<8 and row>1) or (row == 8 and col<4 and col!=0) or (col == 0 and row==7 )):
            str = str+"* "
        else:
            str = str+" "
    str = str+"\n"
print(str)

print("\n")

# print K
str = ""
i=0
j=4
for row in range(7):
    for col in range(7):
        if(col ==0 or (row == col+2 and col>1) ):
            str = str+"* "
        elif((row == i and col ==j)and col>0):
            str = str+"* "
            j= j - 1
            i= i + 1
        else:
            str = str+" "
    str = str+"\n"
print(str)

print("\n")

# print L
str = ""
i=0
j=4
for row in range(7):
    for col in range(8):
        if((col ==1) or (row == 6 and col<5 and col>1 )):
            str = str+"* "
        elif(row == i and col== j and col<0):
            str = str+"* "
            j= j - 1
            i= i + 1
        else:
            str = str+" "
    str = str+"\n"
print(str)

print("\n")

# print M
str = ""
for row in range(7):
    for col in range(7):
        if((col ==0 or col == 6 ) or ((row ==col) and (col>0 and col<4)) or (row==1 and col==5) or (row ==2 and col ==4)):
            str = str+"*"
        else:
            str = str+" "
    str = str+"\n"
print(str)
print("\n")

# print N
str = ""
for row in range(7):
    for col in range(7):
        if((col ==0 or col == 6 ) or (row ==col) ):
            str = str+"*"
        else:
            str = str+" "
    str = str+"\n"
print(str)

print("\n")

# print O
str = ""
for row in range(7):
    for col in range(8):
        if(((row==0 or row==6) and (col<5 and col>1))or (col == 7 and (row!=0 and row!=6 ))or (col == 0 and (row!=0 and row!=6 ))):
            str = str+"* "
        else:
            str = str+" "
    str = str+"\n"
print(str)

print("\n")

# print P
str = ""
for row in range(7):
    for col in range(8):
        if(col==1 or ((row==0 or row==3) and (col<5 and col>1))or (col == 7  and (row!=0 and row!=3 and row<4))):
            str = str+"* "
        else:
            str = str+" "
    str = str+"\n"
print(str)
print("\n")

# print Q
str = ""
for row in range(7):
    for col in range(8):
        if((col == 1 and (row!=0 and row!=6 )) or ((row==0 or row==6) and (col<5 and col>1))or (col == 7 and (row!=0 ))):
            str = str+"* "
        else:
            str = str+" "
    str = str+"\n"
print(str)

print("\n")

# print R
str = ""
for row in range(7):
    for col in range(8):
        if(col==1 or ((row==0 or row==3) and (col<5 and col>1))or (col == 7  and (row!=0 and row!=3))):
            str = str+"* "
        else:
            str = str+" "
    str = str+"\n"
print(str)
print("\n")

# print S
str = ""
for row in range(7):
    for col in range(8):
        if((col ==0 and(row<3 and row >0))or(col ==7 and(row<6 and row >3))or ((row == 0 and(col<4 and col>0)) or (row == 3 and(col<4 and col>0)) or (row == 6 and(col<4 and col>0)))):
            str = str+"* "
        else:
            str = str+" "
    str = str+"\n"
print(str)

print("\n")

# print T
str = ""
for row in range(7):
    for col in range(5):
        if((row ==0 ) or (col == 4 and row<7 and row>0 )):
            str = str+"* "
        else:
            str = str+" "
    str = str+"\n"
print(str)

print("\n")

# print U
str = ""
for row in range(7):
    for col in range(8):
        if(((row==6) and (col<5 and col>0))or (col == 7 and (row!=0 and row!=6 ))or (col == 0 and (row!=0 and row!=6 ))):
            str = str+"* "
        else:
            str = str+" "
    str = str+"\n"
print(str)

print("\n")

# print V
str = ""
i = 0
j = 8
for row in range(5):
    for col in range(9):
        if(col==row):
            str =  str+"* "
        elif((row == i and col ==j)):
            str = str+"* "
            j= j - 1
            i= i + 1
        else:
            str = str+" "
    str = str+"\n"
print(str)
print("\n")

# print W
str = ""
for row in range(7):
    for col in range(9):
        if((col ==0 or col == 8 ) or (col == 2 and row == 5 ) or (col==3 and row ==4 ) or (col ==4 and row == 3) or (col == 5 and row == 4 ) or (col==6 and row ==5)):
            str = str+"*"
        else:
            str = str+" "
    str = str+"\n"
print(str)
print("\n")

# print X
str = ""
i = 0
j = 6
for row in range(7):
    for col in range(6):
        if(col==j or row== i):
            str = str+"* "
            i=i+1
            j=j-1
        elif(col == row):
            str = str+"* "
        else:
            str = str+" "
    str = str+"\n"
print(str)
print("\n")







