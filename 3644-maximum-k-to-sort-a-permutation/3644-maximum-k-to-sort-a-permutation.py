class Solution:
    def sortPermutation(self, nums: List[int]) -> int:
        n=len(nums)
        if all(i==nums[i] for i in range(n)):
            return 0

        k=None
        for v,i in enumerate(nums):
            if(v!=i):
                if(k==None):
                    k=v
                k=k&v

        return k