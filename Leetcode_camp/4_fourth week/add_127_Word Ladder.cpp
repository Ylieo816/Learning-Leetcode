class Solution {
public:
    int ladderLength(string beginWord, string endWord, vector<string>& wordList) {
        unordered_set<string> dic(wordList.begin(),wordList.end());
        queue<string> q;
        q.push(beginWord);
        int step = 1;
        while(!q.empty()){
            int n=q.size();
            for(int k=0; k<n; k++){
                string data = q.front();
                q.pop();
                if(data == endWord){
                    return step;       
                }

                dic.erase(data);

                for(int i=0; i<data.size(); i++){
                    char c = data[i];
                    for(int j=0; j<26; j++){
                        data[i] = 'a'+j;
                        if(dic.find(data) != dic.end()){
                            q.push(data);
                        }
                    }
                    data[i] = c;
                }
            }
            step++;
        }
        return 0;
    }
};