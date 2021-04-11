class Solution {
public:
    uint32_t reverseBits(uint32_t n) {
        uint32_t an=0;
        for(int i=0; i<32; i++){
            an<<=1;
            an = an | (n&1);
            n>>=1;
        }
        return an;
    }
};