class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        se = set(nums)
        if len(se) != len(nums):
            return True
        return False