import sys
input = sys.stdin.readline



for _ in range(int(input())):
    W, N =  map(int, input().split())
    X, w = 0, W
    for _ in range(N):  
        x_i, w_i =  map(int, input().split())
        if w - w_i < 0: 
            X += x_i*2
            w = W - w_i
        elif w - w_i == 0: 
            X += x_i*2
            w = W
        else:
            w -= w_i
    if w != W: 
        X += x_i*2

    print(X)