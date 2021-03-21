class Solution {
public:
    int climbStairs(int n) {
        // answer1: while loop
        int first_step = 1;
        int second_step = 2;
        if (n <= 2){
            return n;
        }
        
        for(int i = 3; i<=n; i++){
            int t = first_step + second_step;
            first_step = second_step;
            second_step = t;
        }
        return second_step;
        
        //answer2: recursion
//         if(n == 1){
//             return 1;
//         }else if(n == 2){
//             return 2;
//         }
//         int answer = climbStairs(n-1) + climbStairs(n-2);
        
//         return answer;
    }
};