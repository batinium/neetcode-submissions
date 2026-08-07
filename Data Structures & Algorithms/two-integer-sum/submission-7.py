class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        hashmap = defaultdict(int)


        for i in range(0,len(nums)):
            j = target - nums[i]
            if j in hashmap:
                return [hashmap[j],i]
            else:
                hashmap[nums[i]] = i