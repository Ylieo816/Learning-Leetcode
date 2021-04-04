class Solution {
public:
    int hammingWeight(uint32_t n) {
        int answer = 0;
        // first answer;
        // while(n){
        //     answer += n & 1;
        //     n>>=1;
        // }
        // second answer;
        while(n){
            n = n&(n-1);
            answer++;
        }
        return answer;
    }
};