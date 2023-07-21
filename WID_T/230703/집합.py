from sys import stdin

m = int(stdin.readline())
s = []

def add():
    if int(cmd[1]) in s:
        pass
    else:
        s.append(int(cmd[1]))
        
def remove():
    if int(cmd[1]) not in s:
        pass
    else:
        s.remove(int(cmd[1]))
        
def check():
    print(1 if int(cmd[1]) in s else 0)
    
def toggle():
    if int(cmd[1]) in s:
        s.remove(int(cmd[1]))
    else:
        s.append(int(cmd[1]))
        
def all():
    global s
    s = [i for i in range(1, 21)]
    
def empty():
    global s
    s = []
    
for i in range(m):
    cmd = stdin.readline().split()
    if cmd[0] == 'add':
        add()
    elif cmd[0] == 'remove':
        remove()
    elif cmd[0] == 'check':
        check()
    elif cmd[0] == 'toggle':
        toggle()
    elif cmd[0] == 'all':
        all()
    elif cmd[0] == 'empty':
        empty()