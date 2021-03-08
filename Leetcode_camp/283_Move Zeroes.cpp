class Solution {
public:
    void moveZeroes(vector<int>& nums) {
        int i_zero = 0, i_nonzero = 0;
        while(i_zero < nums.size() and i_nonzero < nums.size()){
            if(nums[i_nonzero] != 0){
                swap(nums[i_nonzero],nums[i_zero]);
                i_nonzero++;
                i_zero++;
            }else{
                i_nonzero++;
            }
        }
    }
};