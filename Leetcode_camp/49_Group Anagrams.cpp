class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        vector<vector<string>> answer;
        map<string,vector<string>> dic;
        for(auto s:strs){
            string value = s;
            sort(value.begin(), value.end());
            dic[value].push_back(s);
        }
        for(auto v:dic){
            answer.push_back(v.second);
        }
        return answer;
    }
};