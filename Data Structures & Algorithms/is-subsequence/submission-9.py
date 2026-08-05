class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True

        i,j = 0,0

        for j in range(0,len(t)):

            if t[j] == s[i]:
                i+=1
            if i== len(s):
                return True
        return False