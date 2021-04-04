class Solution {
public:
    int maxProduct(vector<int>& nums) {
        int formax =nums[0], formin =nums[0], sofar=nums[0];
        for(int i=1; i<nums.size();i++){
            if(nums[i]<0){
                swap(formax,formin);
            }
            
            formax = max(formax*nums[i],nums[i]);
            formin = min(formin*nums[i],nums[i]);
            
            sofar = max(formax,sofar);
        }
        return sofar;
    }
};