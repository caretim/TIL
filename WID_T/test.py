n = input()

result= set()



for i in range(0, len(n)) : 
  for j in range(i+1, len(n)+1) : 
   result.add("".join(n[i:j]))


