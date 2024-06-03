import sys
input= sys.stdin.readline
def div5(cn):
	cnt= 0
	while cn>= 5:
		cn//= 5
		cnt+= cn
	return cnt
	
def div2(cn):
	cnt= 0
	while cn>= 2:
		cn//= 2
		cnt+= cn
	return cnt

n, k= map(int, (input().rstrip()).split())
print(min(div5(n)- div5(n- k)- div5(k), div2(n)- div2(n- k)- div2(k)))
