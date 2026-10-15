class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        n=len(nums)
        s=0
        for f in range(1,n):
            if(nums[f]!=nums[s]):
                s+=1
                nums[s]=nums[f]

        return s+1