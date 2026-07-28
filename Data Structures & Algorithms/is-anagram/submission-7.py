class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        letter_counts ={}

        for item in s:
            if item in letter_counts:
                letter_counts[item] +=1
            else:
                letter_counts[item] = 1
        
        for letter in t:
            if letter not in letter_counts:
                return False
            else:
                letter_counts[letter] -=1
                if letter_counts[letter] < 0:
                    return False
        
        return True


