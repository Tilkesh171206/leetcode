class Solution:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        res=list()
        n=len(nums)
        nums=set(nums)
        for i in range(1,n+1):
            if i in nums:
                continue
            else:
                res.append(i)

        return res