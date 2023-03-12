from collections import deque

T = int(input())
ans = []
for b in range(T):
  cnt = 0; sta = False
  arr = list(input())
  n = int(input())
  string = input()
  if n > 0:
    string = string.replace('[', "").replace("]", "")
    str_list = list(map(int, string.split(',')))
  else: str_list = []
  ans_list = deque(str_list)
  func = [0]*(400001)
  func[0] = arr[0]
  k = 0
  
  for i in range(len(arr)-1):
    if arr[i] == arr[i+1]:
      func[k] = func[k] + arr[i+1]
    else:
      k += 1
      func[k] = arr[i+1]

  for i in func:
    if i == 0:
      if cnt % 2 == 0:
        ans.append("[" + str(','.join(map(str,ans_list))) + "]")
        break
      else:
        ans_list.reverse()
        ans.append("[" + str(','.join(map(str,ans_list))) + "]")
        break
    if 'R' in i:
      cnt += len(i)
    if 'D' in i:
      if cnt % 2 == 0:
        for j in range(len(i)):
          if len(ans_list) == 0:
            ans.append('error')
            break
          else:
            ans_list.popleft()
            if j == len(i)-1 and len(ans_list) == 0:
              ans.append("[" + str(','.join(map(str,ans_list))) + "]")
              break
        if len(ans_list) == 0:break
      else:
        for j in range(len(i)):
          if len(ans_list) == 0:
            ans.append('error')
            break
          else: 
            ans_list.pop()
            if j == len(i)-1 and len(ans_list) == 0:
              ans.append("[" + str(','.join(map(str,ans_list))) + "]")
              break
        if len(ans_list) == 0: break

for i in range(len(ans)):
  print(ans[i])