class Solution {
public:
    int maximalSquare(vector<vector<char>>& matrix) {
        int r=matrix.size(), c=matrix[0].size();
        int dp[r][c];
        int border = 0;
        for(int i=0; i<r;i++){
            for(int j=0;j<c;j++){
                if(i==0 or j==0 or matrix[i][j]=='0'){
                    dp[i][j] = matrix[i][j]-'0';
                }else{
                    dp[i][j] = min(dp[i-1][j-1],min(dp[i-1][j],dp[i][j-1])) +1;
                }
                border = max(border, dp[i][j]);
            }
        }
        return border*border;
    }
};