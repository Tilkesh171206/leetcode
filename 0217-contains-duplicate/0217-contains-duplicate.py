class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        nums.sort()
        n=len(nums)
        for j in range(1,n):
            if(nums[j-1]==nums[j]):
                return True
        return False