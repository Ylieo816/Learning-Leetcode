class Solution {
public:
    string getHint(string secret, string guess) {
        int secret_len = secret.size();
        int guess_len = guess.size();
        int corret = 0, error = 0;
        int g[10] = {0},s[10] = {0};
        
        for(int i=0; i<secret_len; ++i){
            if(secret[i] == guess[i]){
                corret++;
            }else{
                s[secret[i] - '0']++; 
                g[guess[i] - '0']++;
            }
        }
        for(int i=0; i<10;++i){
            if(s[i]<g[i]){
                error += s[i];
            }else{
                error += g[i];
            }
        }
        return to_string(corret)+"A"+to_string(error)+"B";
        
        
        
    }
};