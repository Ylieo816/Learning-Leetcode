class Solution {
public:
    int firstUniqChar(string s) {
        int arr[26], ad[26];
        memset(arr,0,sizeof(arr));
        memset(ad,-1,sizeof(arr));
        int l = s.size();
        for(int i=0; i<l;i++){
            arr[s[i]-'a']++;
            if(ad[s[i]-'a']==-1){
                ad[s[i]-'a'] = i;
            }
        }
        int index = INT_MAX;
        for(int i=0; i<26; i++){
            if(arr[i]==1 and ad[i]!=-1 and ad[i]<index){
                index = ad[i];
            } 
        }
        return (index==INT_MAX)? -1:index;
    }
};