class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        seen={0:1}
        r_sum=0
        ret=0

        for n in nums:
            r_sum+=n

            target=r_sum-k

            if(target in seen):
                ret+=seen[target]


            seen[r_sum]=seen.get(r_sum,0)+1

        return ret