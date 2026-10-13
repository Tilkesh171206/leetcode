class Solution {
public:
    long long maximumSubarraySum(vector<int>& nums, int k) {
        long long maxsum = 0;
        long long current = 0;
        unordered_set<int> seen;
        int n = nums.size();
        int left = 0;
        for (int right = 0; right < n; ++right) {
            while (seen.count(nums[right])) {
                seen.erase(nums[left]);
                current -= nums[left];
                left++;
            }
            seen.insert(nums[right]);
            current += nums[right];

            if (right - left + 1 > k) {
                seen.erase(nums[left]);
                current -= nums[left];
                left++;
            }
            if (right - left + 1 == k) {
                maxsum = max(maxsum, current);
            }
        }
        return maxsum;
    }
};