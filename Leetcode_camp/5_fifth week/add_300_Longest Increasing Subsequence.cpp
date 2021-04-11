class Solution {
public:
    int lengthOfLIS(vector<int>& nums) {
        int l = nums.size();
        vector<int> dp(l,1);
        // dp[0] = 1;
        for(int i=1; i<l;i++){
            for(int j=0; j<i; j++){
                if(nums[i]>nums[j]){
                    dp[i] = max(dp[i], dp[j]+1);
                }
            }
        }
        for(int i=0; i<l; i++){
            printf("%d ",dp[i]);
        }
        return *max_element(dp.begin(), dp.end());
    }
};