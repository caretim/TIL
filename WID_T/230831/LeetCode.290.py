class Solution(object):
    def wordPattern(pattern, s):
        dict1 ={}
        dict2 ={}
        s= list((s.split(' ')))
        for p,w in zip(pattern,s):
            if p not in dict1 and w not in dict2:
                dict1[p] = w
                dict2[w] = p
            elif p in dict1 and w in dict2:
                if dict1[p] != w or dict2[w] != p:
                    return False
            else:
                return False
        return True 

print(Solution.wordPattern("abc","dog cat dog"))