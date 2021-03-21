class Solution {
public:
    int wiggleMaxLength(vector<int>& nums) {
        bool flag=true;
        int count=0;
        for(int i=1; i<nums.size(); ++i){
            if(count==0 and nums[i]!=nums[i-1]){
                flag = (nums[i-1]>nums[i]);
                count +=1;
            }else if((nums[i-1]<nums[i]) ==flag and count!=0){
                flag = !flag;
                count++;
            }
        }
        return count+1;
    }
};