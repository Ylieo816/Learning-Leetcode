class Solution {
public:
    int climbStairs(int n) {
        if (n <= 2){
            return n;
        }
        int first_step = 1;
        int second_step = 2;
        for(int i = 3; i<=n; i++){
            int t = first_step + second_step;
            first_step = second_step;
            second_step = t;
        }
        return second_step;
    }
};