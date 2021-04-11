class Solution {
public:
    string reverseOnlyLetters(string S) {
        int left=0, right=S.size();
        while(left<right){
            if(!((S[left] >=65 and S[left] <= 90) or(S[left] >=97 and S[left] <= 122))){
                left++;
            }else if(!((S[right] >=65 and S[right] <= 90) or(S[right] >=97 and S[right] <= 122))){
                right--;
            }else{
                char t = S[left];
                S[left] = S[right];
                S[right] = t;
                left++;
                right--;
            } 
        }
        return S;
    }
};