class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        myhash = defaultdict(int)

        for i in arr:
            myhash[i] += 1
        temphash = myhash.copy()
        for i in myhash:
            if myhash[i] > 1:
                temphash.pop(i)
        
        if len(temphash) >= k:
            return str(list(temphash.keys())[k-1])
        else:
            return ""

        
        
        
            
                