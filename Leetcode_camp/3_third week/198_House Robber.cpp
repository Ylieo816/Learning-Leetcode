class Solution {
public:
    int rob(vector<int>& nums) {
        // DP:
        // 因為需在每一格考量是否要取值(搶劫)，因此除了DP值外還要有是否被搶
        // DP[i][0] = max(DP[i-1][0],DP[i-1][1]) --> 判斷前一項的最大值(不論是否搶過)
        // DP[i][1] = DP[i-1][0] + nums[i]  --> 只能取沒被搶的前一項+現在
        // 可簡化成 DP[i] = max(DP[i-1], DP[i-2]+nums[i]) 因為[i-2]包含[i-3]...，所以取2即可
        int l = nums.size();
        
        if(l<=1){
            return l==0? 0:nums[0];
        }
        // answer1:
//         int dp[l][2];
//         dp[0][0] = 0;
//         dp[0][1] = nums[0];
        
//         for(int i=1; i<l; i++){
//             dp[i][0] = max(dp[i-1][0],dp[i-1][1]);
//             dp[i][1] = dp[i-1][0] + nums[i];   
//         }
//         return max(dp[l-1][0],dp[l-1][1]); 
        
        //answer2:
//         int dp[l];
//         dp[0] = nums[0];
//         dp[1] = max(nums[0],nums[1]);
        
//         for(int i=2; i<l; i++){
//             dp[i] = max(dp[i-2]+nums[i],dp[i-1]);
//         }
//         return dp[l-1];
        
        // answer3: optimize 
        int last = 0, now=0;
        for(int i=0; i<l; i++){
            int temp = last;
            last = now;
            now = max(temp+nums[i],now);
        }
        return now;
    }
};