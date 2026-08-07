class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seenmap = defaultdict(int)

        for i in range(0,len(nums)):
            needed = target - nums[i]
            if needed in seenmap:
                return [min(i,seenmap[needed]), max(i,seenmap[needed])]
            else:
                seenmap[nums[i]] = i