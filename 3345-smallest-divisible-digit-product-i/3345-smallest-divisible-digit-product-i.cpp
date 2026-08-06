class Solution {
public:
    int smallestNumber(int n, int t) {
        while(1){
            int m=n;
            int pro=1;
            while(m>0){
            pro=pro*(m%10);
            m=m/10;
            }
            if(pro%t==0){
                return n;
            }
            else{
                n++;
            }
        }
        return 0;
    }
};