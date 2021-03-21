class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        map<int,int> table;
        for(int i=0; i<nums.size(); ++i){
            table[nums[i]]++;
        }
        vector<pair<int,int>> arr;
        for(auto i:table){
            arr.push_back(make_pair(i.second, i.first));
        }
        sort(arr.begin(), arr.end());
        vector<int> answer;
        int l = arr.size();
        for(int i=l-1; i>(l-k-1); --i){
            answer.push_back(arr[i].second);
        }
        return answer;
    }
};