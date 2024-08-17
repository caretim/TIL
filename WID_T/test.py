order = ''
n = int(input())
for _ in range((n*2)-1):
    order += input()
order = order.replace('/', '//')
print(eval(order))