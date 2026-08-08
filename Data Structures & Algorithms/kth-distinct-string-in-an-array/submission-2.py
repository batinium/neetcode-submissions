from collections import Counter

class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        freqmap = {}

        for char in arr:
            freqmap[char] =freqmap.get(char,0) +1
        
        _k = k
        for s in arr:
            if freqmap[s] == 1:
                k -=1
                if k == 0:
                    return s
        return ""

                


        

        
        
        
        
            
                