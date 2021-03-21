class Solution {
public:
    void dfs(vector<vector<int>> &an, vector<int> num, vector<int> now, int index){
        if(index == num.size()){
            an.push_back(now);
            return;
        }
        
        dfs(an,num,now,index+1);
        
        now.push_back(num[index]);
        dfs(an,num,now,index+1);
        
        now.pop_back();
    }
    
    
    vector<vector<int>> subsets(vector<int>& nums) {
        vector<vector<int>> answer;
        if(nums.size()==0){
            return answer;
        }
        dfs(answer,nums, vector<int> (), 0);
        return answer;
    }
};