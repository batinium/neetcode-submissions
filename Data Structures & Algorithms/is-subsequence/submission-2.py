import collections
import bisect

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        mydict = collections.defaultdict(list)
        for i, char in enumerate(t):
            mydict[char].append(i)

        prev_idx = -1

        for char in s:
            if char not in mydict:
                return False
            
            idx_in_list = bisect.bisect_right(mydict[char],prev_idx)

            if idx_in_list == len(mydict[char]):
                return False
            
            prev_idx = mydict[char][idx_in_list]
        return True
        