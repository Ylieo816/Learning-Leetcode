class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        int l = nums.size();
        // answer 1: brute
        // bool flag = false;
        // vector<int> answer;
        // for(int i = 0; i<l; i++){
        //     for(int j = i+1; j<l; j++){
        //         if(nums[i]+nums[j] == target){
                    
        //             answer.push_back(i);
        //             answer.push_back(j);
        //             return answer;
        //         }
        //     }
        // }
        // return answer;

        // answer 2: table 
        unordered_map<int,int> table = {};
        vector<int> answer;
        for(int i = 0; i<l; i++){
            if(table.find(target - nums[i]) != table.end()){
                answer.push_back(table[target - nums[i]]);
                answer.push_back(i);
                break;
            }
            table[nums[i]] = i;
        }
        return answer;
    }
};