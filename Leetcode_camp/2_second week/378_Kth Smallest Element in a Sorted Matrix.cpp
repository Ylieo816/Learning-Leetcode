class Solution {
public:
    int kthSmallest(vector<vector<int>>& matrix, int k) {
        int w = matrix.size(), h = matrix[0].size();
        int arr[w*h];
        for(int i=0; i<w; ++i){
            for(int j=0; j<h; ++j){
                arr[w*i+j] = matrix[i][j];
            }    
        }
        sort(arr, arr+(w*h));
        return arr[k-1];
    }
};