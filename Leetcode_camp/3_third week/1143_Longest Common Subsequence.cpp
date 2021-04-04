class Solution {
public:
    int longestCommonSubsequence(string text1, string text2) {
        int l1 = text1.size(), l2=text2.size();
        if(l1==0 or l2==0){
            return 0;
        }
        
        int arr[l1+1][l2+1];
        memset(arr,0,(l1+1)*(l2+1)*sizeof(int));
        for(int i=1; i<=l1; i++){
            for(int j=1; j<=l2; j++){
                if(text1[i-1]==text2[j-1]){
                    arr[i][j] = arr[i-1][j-1]+1;
                }else{
                    arr[i][j] = max(arr[i-1][j],arr[i][j-1]);
                }
            }
        }
        return arr[l1][l2];
    }
};