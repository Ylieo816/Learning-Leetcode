class Solution {
public:
    bool isValid(string s) {
        int l = s.size();
        if(l%2 != 0 || l ==0){
            return false;
        }        
        map<char,char> table;
        table['('] = ')';
        table['['] = ']';
        table['{'] = '}';
        
        stack<char> mystack;
        for(int i=0; i<l; ++i){
            if((s[i] == '(') or (s[i] == '[') or (s[i] == '{')){
                mystack.push(s[i]);
            }else{
                if(mystack.empty() == true){
                    return false;
                }
                char value = mystack.top();
                if(s[i] != table[value]){
                    return false;
                }
                mystack.pop();
            }
        }
        if(mystack.empty() == true){
            return true;
        }else{
            return false;
        }
    }
};