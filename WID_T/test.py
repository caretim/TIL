class Solution:
    def wordPattern(pattern: str, s: str) -> bool:
        arr = s.split()
        if len(arr) != len(pattern):
            return False
        
        for i in range(len(arr)):
            print(pattern.find(pattern[i]), arr.index(arr[i]))
            if pattern.index(pattern[i]) != arr.index(arr[i]):
                return False
        return True


print(Solution.wordPattern("aba","cat dog dog "))