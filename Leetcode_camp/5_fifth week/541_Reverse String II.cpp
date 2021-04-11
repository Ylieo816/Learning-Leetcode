class Solution {
public:
    string reverseStr(string s, int k) {
        int l = s.size();
        if(l==1){
            return s;
        }
        for(int i=0; i<l; i+=2*k){
            int left = i, right = i+k-1;
            if(right>=l){
                right = l-1;
            }
            while(left<right){
                char t = s[left];
                s[left] = s[right];
                s[right] = t;
                left++;
                right--;
            }
        }
        return s;
    }
};