class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if len(nums) <= 1:
            return False
        
        dupes = {}

        for i in range(0,len(nums)):
            if nums[i] in dupes:
                return True
            else:
                dupes[nums[i]] = 1

        return False