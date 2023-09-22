n =int(input())

ln = len(str(n))
result =0
for i in range(ln):
    an = n%10
    n=n//10
    
    if an>4:
        result+= (an-1)*(9**i)
    else:
        result+= an*(9**i)
print(result)