class Solution {
public:
    bool isAnagram(string s, string t) {
        // sort(s.begin(),s.end());
        // sort(t.begin(),t.end());
        // if(s==t){
        //     return true;
        // }else{
        //     return false;
        // }
        
        if(s.size()!=t.size()){
            return false;
        }
        
        map<char,int> ss;
        for(int i=0; i<s.size(); ++i){
            ss[s[i]]++;
            ss[t[i]]--;
        }
        
        for(auto i:ss){
            if(i.second){
                return false;
            }
        }
        return true;
        
    }
};