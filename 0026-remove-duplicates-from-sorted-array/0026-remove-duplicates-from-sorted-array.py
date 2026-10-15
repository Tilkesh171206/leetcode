class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        if not nums:
           return (0)
        s=0
        for f in range(1,len(nums)):
            if(nums[f]!=nums[s]):
                s+=1
                nums[s]=nums[f]

        return s+1



        #  if not nums:
        #     return (0)
        # k=1
        # for i in range(1,len(nums)):
        #     if nums[i]!=nums[k-1]:    
        #         nums[k]=nums[i]
        #         k+=1
        # return k