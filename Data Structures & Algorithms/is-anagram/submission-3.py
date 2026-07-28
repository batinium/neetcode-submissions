class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        count = {}
        for c in s:
            count[c] = count.get(c,0) + 1
        
        for ce in t:
            if count.get(ce,0):
                count[ce] = count.get(ce) - 1
            else:
                return False
        return True