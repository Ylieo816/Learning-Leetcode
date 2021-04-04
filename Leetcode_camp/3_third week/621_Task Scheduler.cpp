class Solution {
public:
    int leastInterval(vector<char>& tasks, int n) {
        map<char,int> dp;
        int count = 0;
        for(auto e:tasks){
            dp[e]++;
            if(dp[e]>count){
                count = dp[e];
            }
        }
        
        int answer = (count-1) * (n+1);
        for(auto e:dp){
            if(e.second == count){
                answer++;
            } 
        }
        return max((int)tasks.size(),answer);
    }
};