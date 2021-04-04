class Solution {
public:
    bool isPowerOfTwo(int n) {
        return (n>=1 and (n&(n-1))==0)? true:false;
        // answer1
        // double an = (double)n;
        // while((an/2)>=1){
        //     an /=2;
        //     printf("%lf\n",an);
        // }
        // return (an==1)? true:false;
    }
};  