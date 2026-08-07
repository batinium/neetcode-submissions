class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seenmap = defaultdict(int)

        for m in range(0,len(nums)):
            n = target - nums[m]

            if n in seenmap:
                return [seenmap[n], m]
            else:
                seenmap[nums[m]] = m