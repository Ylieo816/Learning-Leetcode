class Solution {
public:
    vector<int> plusOne(vector<int>& digits) {
        int l = digits.size();
        int plus = 1;
        for(int i = l-1; i>=0; i--){
            if(digits[i] != 9 && plus ==1){
                digits[i]++ ;
                plus = 0;
                break;
            }else{
                digits[i] = 0;
                if(i==0){
                    digits.insert(digits.begin(),1);
                }
            }
        }
        return digits;
    }
};