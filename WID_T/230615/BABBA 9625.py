
n= int(input())

# B -> BA ->BAB ->BABBA->BA B BA BA B

# B-> BA , A->B

#B일때. B=1 A= 1
#A일때 B =1

A=0
B=1
for __ in range(n-1):
    NA = B
    NB = A+B
    A=NA
    B=NB

print(A,B)

 