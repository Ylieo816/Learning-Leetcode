class Solution {
public:
    bool isPerfectSquare(int num) {
        // answer1: newton 
        // long v = num;
        // while(v*v>num){
        //     v = (v+num/v)/2;
        // }
        // return v*v==num;
        
        //answer2: BS
        long low = 1, high = num;
        while(low<=high){
            long mid = (low+high)/2; 
            if(mid*mid == num){
                return true;
            }else if(mid*mid > num){
                high = mid-1;
            }else{
                low = mid+1;
            }
        }
        return false;
        
        
        
    }
};