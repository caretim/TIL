tokens =["2","1","+","3","*"]
stack=[]
oper = ['+','-','*','/']
for i in tokens:
    if i not in oper:
        stack.append(int(i))
    else:
        num1 ,num2 = stack.pop(),stack.pop()
        if i == '-':
            stack.append(num1-num2)
        elif i == '+':
            stack.append(num1+num2)
        elif i == '/':
            stack.append(num1/num2)
        elif i == '*':
            print(num1,num2)
            stack.append(num1*num2)
        
print(stack)
    
