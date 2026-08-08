import collections
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mydict = defaultdict(int)
        
        for n in nums:
            mydict[n] +=1
        return heapq.nlargest(k, mydict.keys(), key=mydict.get)
        
        



            


        