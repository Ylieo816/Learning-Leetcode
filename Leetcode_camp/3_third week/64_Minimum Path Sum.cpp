class Solution {
public:
    int minPathSum(vector<vector<int>>& grid) {
        int r = grid.size(), c = grid[0].size();
        // int arr[r][c];        
        // arr[0][0] = grid[0][0];
        // for(int i=1; i<r;i++){
        //     arr[i][0] = arr[i-1][0] + grid[i][0];
        // }
        // for(int i=1; i<c;i++){
        //     arr[0][i] = arr[0][i-1] + grid[0][i];
        // }
        // for(int i=1; i<r; i++){
        //     for(int j=1; j<c; j++){
        //         arr[i][j] = min(arr[i-1][j], arr[i][j-1]) + grid[i][j];
        //     }
        // }
        // return arr[r-1][c-1];
        // optimize answer
        int arr[c];        
        arr[0] = grid[0][0];
        for(int i=1; i<c;i++){
            arr[i] = arr[i-1] + grid[0][i];
        }
        
        for(int i=1; i<r; i++){
            arr[0] += grid[i][0];
            for(int j=1; j<c; j++){
                arr[j] = min(arr[j-1], arr[j]) + grid[i][j];
            }
        }
        return arr[c-1];
    }
};