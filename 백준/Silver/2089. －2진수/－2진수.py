number = int(input())
if number == 0 :
  print(0)
else:
  d = number
  result = ""
  while d != 1:
    r = d % -2
    d = d // -2
    if r < 0:
      d += 1
      r *= (-1)
    result += str(r)
  else:
    result += str(d)
  print(result[::-1])