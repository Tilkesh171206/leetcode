class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        res=0
        n=len(nums)
        for i in range(n):
            for j in range(i,n):
                sub=[]
                sub=nums[i:j+1]
                s=set(sub)
                res+=len(s)*len(s)

        return res