class a():
    def __init__(self,num):
        self.num = num



b = a(1)

c = b


c.num = 2


print(b.num)