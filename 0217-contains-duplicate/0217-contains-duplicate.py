class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        nums.sort()
        n=len(nums)
        j=1
        while(j<n and n>1):
            if(nums[j-1]==nums[j]):
                return True
            else:
                j=j+1
        return False