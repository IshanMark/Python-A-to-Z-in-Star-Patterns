
# print A
from this import d


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