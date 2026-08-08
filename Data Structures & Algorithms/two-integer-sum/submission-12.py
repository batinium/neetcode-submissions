class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seenmap = defaultdict(int)

        for i in range(0,len(nums)):
            j = target - nums[i]
            if j in seenmap:
                return [seenmap[j],i]
            else:
                seenmap[nums[i]] = i