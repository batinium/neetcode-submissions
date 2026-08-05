class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        iter_amount = 0
        for i in range(len(s)-1,-1,-1):
            if s[i] == " " and iter_amount == 0:
                continue 

            elif s[i] != " ":
                iter_amount+=1
            else:
                return iter_amount
        return len(s)
