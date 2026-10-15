class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        if not nums:
            return 0

        write =0

        for num in nums:

            if write<2 or num!=nums[write-2]:
                nums[write]=num
                write+=1
    
        return write
