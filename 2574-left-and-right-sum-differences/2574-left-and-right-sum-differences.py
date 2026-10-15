class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        n=len(nums)
        left_sum=[None] * n
        right_sum=[None] * n
        
        #left sum 
        l=0
        for i in range(n):
            if i==0 :
                left_sum[i]=0
                l=nums[i]
            else:
                left_sum[i]=l
                l=l+nums[i]

        # right sum
        r=0
        for i in range(n-1,-1,-1):
            if i==n-1 :
                right_sum[i]=0
                r=nums[i]
            else:
                right_sum[i]=r
                r=r+nums[i]

        for i in range(n):
            nums[i]=abs(left_sum[i]-right_sum[i])

        return nums

