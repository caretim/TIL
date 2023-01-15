def h(n,height):
    if n>height:
        r = n
    return r


def solution(array, height):
    a =list(map(h,array))
    return len(a)