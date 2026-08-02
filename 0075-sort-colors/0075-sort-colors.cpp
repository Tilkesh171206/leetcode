class Solution {
public:
    void sortColors(vector<int>& nums) {
        int n=nums.size();
        int left=0;
        int right=n-1;
        while(left<right){
            if(nums[left]>nums[right]){
                swap(nums[left],nums[right]);
                if(nums[right]==2){
                    right--;
                }
                if(nums[left]==0){
                    left++;
                }
            }
            else if(nums[left]==nums[right]){
                if(nums[left]>=nums[left+1]){
                    right--;
                }else{
                    left++;
                }
            }
            else if(nums[left]==0){
                left++;
            }
            else if(nums[right]==2){
                right--;
            }
            
        }
    }
};