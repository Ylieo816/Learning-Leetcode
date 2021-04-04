class Solution {
public:
    int uniquePathsWithObstacles(vector<vector<int>>& obstacleGrid) {
        int l = obstacleGrid.size(), r = obstacleGrid[0].size();
        if(obstacleGrid[l-1][r-1]==1){
            return 0;
        }
        
        long arr[l+1][r+1];
        memset( arr, 0, (l+1)*(r+1)*sizeof(long) );
        arr[l-1][r-1]=1;
        for(int i=l-1; i>=0; i--){
            for(int j=r-1; j>=0; j--){
                if(arr[i][j]==0 and obstacleGrid[i][j]==0){
                    arr[i][j] = arr[i][j+1] + arr[i+1][j];
                }
            }
        }
        return arr[0][0];
    }
};