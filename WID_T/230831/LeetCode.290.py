class Solution(object):
    def wordPattern(pattern, s):
        dict ={}
        s= list((s.split(' ')))
        for p,w in zip(pattern,s):
            if p not in dict and w not in dict:
                dict[p] = w
                dict[w] = p
                print(p,w)
            elif p in dict and w in dict:
                if dict[p] != w or dict[w] != p:
                    print(p,w ,dict[p],dict[w])
                    return False
            else:
                return False
        return True 

print(Solution.wordPattern("abc","dog cat dog"))