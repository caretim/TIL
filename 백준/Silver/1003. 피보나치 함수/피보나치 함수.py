for tc in range(int(input())):
    n = int(input())
    zero = 1
    one = 0
    temp =0
    for __ in range(n):
        temp= one
        one = one+ zero
        zero = temp
    print(zero,one)
    