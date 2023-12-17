# x, y, d, t = map(int, input().split())


# # 직사각형의 대각선 길이(피타고라스)

# dist = (x**2 + y**2) ** 0.5



# if t > d:
#     print(dist)
#     # t가 d보다 작을경우, 직선거리로 이동

# else:
#     n = dist // d
#     print(min(t*n+dist-d*n,t*(n+1) if d<dist else min(dist,t+d-dist,2*t)))
#     # print(t * (dist // d))
#     # print(dist % d)
#     # print(min(t * (dist // d) + (dist % d), t * ((dist // d) + 1) + (dist % d)))
#     # # d범위의 한계치에서 플러스 마이너스 1회 추가,




x, y, d ,t = map(int,input().split())
dist = (x**2 + y**2) ** 0.5


result = dist      
if d <= t: 
    print(result)

else:
    jump = dist//d
    if jump == 0:
        result = min(result, t+(d-dist))
        result = min(result, (jump+2)*t)
    else:
        rest = dist - ((jump)*d)
        result = min(result, jump*t + rest)
        result = min(result, (jump+1)*t + (d-rest))
        result = min(result, (jump+1)*t )

print(result)