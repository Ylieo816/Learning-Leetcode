class Solution {
public:
    int rob(vector<int>& nums) {
        // 198題+考慮 第一個不偷or最後一個不偷
        int l = nums.size();
        
        if(l<=1){
            return l==0? 0:nums[0];
        }
        // 不搶第一個:
        int last = 0, now=0;
        for(int i=1; i<l; i++){
            int temp = last;
            last = now;
            now = max(temp+nums[i],now);
        }
        int nofirst = now;
        
        //不搶最後一個
        last = 0, now=0;
        for(int i=0; i<l-1; i++){
            int temp = last;
            last = now;
            now = max(temp+nums[i],now);
        }
        
        return max(now,nofirst);;  
    }
};