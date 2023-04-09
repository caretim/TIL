oper=1
arr=[]

for o in oper:
    r = arr[0]
    for k in range(len(arr)-1):
        if o[k]=='+':
            r += arr[k+1]
        elif o[k]=='-':
            r -= arr[k+1]
        elif o[k]=='*':
            r *= arr[k+1]
        else:
            if r//arr[k+1] <0:
                r = -(-r//arr[k+1])
            else:
                r = r//arr[k+1]

    result.append(r)