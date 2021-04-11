class Solution {
public:
    void addpar(vector<string> &value, string s,int left, int right, int max){
        if(s.size() == 2*max){
            value.push_back(s);
            return;
        }
        
        if(left < max){ 
            addpar(value, s+"(", left+1, right,max);
        }
        if(right < left){
            addpar(value, s+")", left, right+1, max);
        }
        
    }
    vector<string> generateParenthesis(int n) {
        vector<string> answer;
        addpar(answer, "", 0, 0, n);
        return answer;
    }
};