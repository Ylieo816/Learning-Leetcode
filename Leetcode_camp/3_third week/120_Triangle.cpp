class Solution {
public:
    int minimumTotal(vector<vector<int>>& triangle) {
        int l = triangle.size();
        if(l==1){
            return triangle[0][0];
        }
        int arr[l];
        for(int i=0; i<l; i++){
            arr[i] = triangle[l-1][i];
        }
        for(int i=l-2; i>=0; i--){
            for(int j=0; j<(triangle[i].size()); j++){
                arr[j] = triangle[i][j] + min(arr[j],arr[j+1]);
            }
        }
        return arr[0];
    }
};