import math

def f(x,k,a):
    return -(a*x/k)+a

x,y,c=map(float,input().split())
l=0
r=x if(x<y) else y

for i in range(100):
    k=(r+l)/2
    a=math.sqrt(x*x-k*k)
    b=math.sqrt(y*y-k*k)
    c0=k*c/b

    if(f(c0,k,a)>c): l=k
    else: r=k
print("%.3f" % l)