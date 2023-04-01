bracket = input()
length = len(bracket)
stack = []
result = 1
res = 0

for i in range(length):
    b = bracket[i]   
    if b == '(':
        result *= 2
        stack.append(b)
    elif b == '[':
        result *= 3
        stack.append(b)

    elif b == ')':
        if not stack or stack[-1] == '[':
            res = 0
            break
        if bracket[i-1] == '(':
            res += result
        result //= 2
        stack.pop()  
    else:
        if not stack or stack[-1] == '(':
            res = 0
            break
        if bracket[i-1] == '[':
            res += result
        result //= 3
        stack.pop() 

if stack:
    res = 0
print(res)