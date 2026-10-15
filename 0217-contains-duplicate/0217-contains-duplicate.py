class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        mums=set(nums)
        n=len(nums)
        m=len(mums)
        if(n==m):
            return False
        return True

        