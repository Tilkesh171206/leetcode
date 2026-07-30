class Solution {
public:
    bool isPalindrome(string s) {
        bool empty=true;
        for(char c:s){
            if(c==' ') {
                continue;
            }
            else{
                empty=false;
            }
        }
        if(empty) return true;

        vector<char>r;
        for(char c:s){
            if((c>='a' && c<='z')||(c>='A'&&c<='Z')||(c >='0' && c <='9')){
                r.push_back(tolower(c));
            }
        }
        int left=0,right=r.size()-1;
        while(left<right){
            if(r[right]!=r[left]){
                return false;
            }
            left++;
            right--;
        }
        return true;
        }
    };