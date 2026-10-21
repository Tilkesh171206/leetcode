class Solution:
    def minOperations(self, s: str) -> int:
        n=len(s)

        if all(s[i-1]<=s[i] for i in range(1,n)):
            return 0

        if n==2:
            return -1
        
        mn,mx=min(s),max(s)
        if(mn==s[0] or mx==s[n-1]):
            return 1


        if any(c==mn or c==mx for c in s[1:-1]):
            return 2
        
        return 3
        