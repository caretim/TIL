n =int (input ())

numls = []

for i in range(n):
    k= int(input())
    if k != 0 :
        numls.append(k)
    elif k == 0:
        numls.pop()


print(sum(numls))