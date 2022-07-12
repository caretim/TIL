a,b = input().split()
a= int(a)
b= int(b)

print(bool(not a and not b) or bool(a and b))