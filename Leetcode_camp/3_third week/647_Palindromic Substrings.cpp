class Solution {
public:
    int countSubstrings(string s) {
        // shorter brute answer:
        int l=s.size();
        int count = 0;
        for(int i=0; i<(2*l-1);i++){
            int left = i/2;
            int right = left + i%2;
            while(left>=0 && right<l && s[left]==s[right]){
                left--;
                right++;
                count++;
            }
        }
        return count;
    }
};