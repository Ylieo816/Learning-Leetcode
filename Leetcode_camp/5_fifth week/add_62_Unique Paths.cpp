class Solution {
public:
    int uniquePaths(int m, int n) {
        // answer1: m*n space
        // int arr[m+1][n+1];
        // memset( arr, 0, (m+1)*(n+1)*sizeof(int) );
        // arr[m-1][n-1]=1;
        // for(int i=m-1; i>=0; i--){
        //     for(int j=n-1; j>=0; j--){
        //         if(arr[i][j]==0){
        //             arr[i][j] = arr[i][j+1] + arr[i+1][j];
        //         }
        //     }
        // }
        // return arr[0][0];
        
        // optimize answer2:
        int arr[n+1];
        memset(arr, 0,(n+1)*sizeof(int));
        for(int i=m-1; i>=0; i--){
            for(int j=n-1; j>=0; j--){
                if(i==(m-1) or j==(n-1)){
                    arr[j] = 1;
                }else{
                    arr[j] = arr[j]+arr[j+1];
                }
            }
        }
        return arr[0];
    }
};