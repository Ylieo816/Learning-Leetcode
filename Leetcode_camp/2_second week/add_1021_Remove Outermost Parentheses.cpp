class Solution {
public:
    string removeOuterParentheses(string S) {
        int count = 0;
        string answer;
        for(int i=0; i<S.size(); ++i){
            if(S[i] == '(' and count++ >0){
                answer += S[i];
            }else if (S[i] == ')' and count-->1){
                answer += S[i];
            }
        }
        return answer;
    }
}; 