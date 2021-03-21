class Solution {
public:
    int mySqrt(int x) {
        // answer1: while
        long r = x;
        while(r*r>x){
            r = (r+x/r)/2;
        }
        return r;

    }
};