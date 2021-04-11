class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int extend = nums[0], sofar =nums[0];
        for(int i=1; i<nums.size(); ++i){
            extend = max(nums[i],extend+nums[i]);
            sofar = max(extend,sofar);
        }
        return sofar;
        
        // DP optimize answer;
        // vector<int> dp = nums;
        // for(int i=1; i<nums.size(); i++){
        //     dp[i] = max(0, dp[i-1])+nums[i];
        // }
        // return *max_element(dp.begin(),dp.end());
    }
};