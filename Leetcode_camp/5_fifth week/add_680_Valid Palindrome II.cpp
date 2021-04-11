class Solution {
public:
    bool validPalindrome(string s) {
        int count = 0;
        int left=0, right = s.size()-1;
        int reg_l, reg_r;
        while(left<right){
            if(s[left] == s[right]){
                left++;
                right--;
            }else{
                if(right-left==1){
                    break;
                }else if((s[left] == s[right-1]) and count<1){
                    reg_l = left;
                    reg_r = right;
                    left++;
                    right -= 2;
                    count = 1;
                }else if((s[left+1] == s[right]) and count<1){
                    reg_l = left;
                    reg_r = right;
                    left +=2;
                    right --;
                    count = 2;
                }else if(count==1){
                    left = reg_l+2;
                    right = reg_r-1;
                    count = 3;
                }else if(count==2){
                    left = reg_l+1;
                    right = reg_r-2;
                    count = 3;
                }else{
                    return false;
                }
            }
        }
        return true;
    }
};