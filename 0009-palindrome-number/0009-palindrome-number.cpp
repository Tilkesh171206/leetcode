class Solution {
public:
    bool isPalindrome(int x) {
        int z=x;
        if(x<0){
            return false;
            }
        long long y=0;
        while(x>0){
            y=y*10+x%10;
            x=x/10;
        }
        if(z==y){
            return true;
            }
        return false;
    }
};