class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        sum=0
        count=0
        for i in range(len(nums)):
            sum=sum+nums[i]
            count=count+i+1
        return count-sum

    