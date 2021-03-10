class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        int l = nums.size();
        vector<vector<int>> answer;
        std::sort(nums.begin(),nums.end());
        
        for(int i=0; i<(l-2);i++){
            int target = -nums[i];
            int left = i+1;
            int right = l-1;
            while(left < right){
                int sum = nums[left]+nums[right];
                if(sum < target){
                    left++;
                }else if(sum > target){
                    right--;
                }else{
                    vector<int> temp = {nums[i],nums[left],nums[right]};
                    answer.push_back(temp);
                    while(left<right && nums[left]==temp[1]){
                        left++;
                    }
                    while(left<right && nums[right]==temp[2]){
                        right--;
                    }
                }
            }
            while(i < (l-1) && nums[i]==nums[i+1]){
                i++;
            }
        }
        return answer;
        
    }
};