class Solution {
public:
    int myAtoi(string s) {
        int len = s.size();
        if(len<1){
            return 0;
        }
        int i=0;
        while(s[i]==' '){
            i++;
        }
        bool sign = true;
        if(s[i]=='-'){
            sign = false;
            i++;
        }else if(s[i]=='+'){
            sign = true;
            i++;
        }
        string answer = "";
        while((s[i]-'0') >=0 and (s[i]-'0') <=9){
            answer += s[i];
            i++;
        }
        // printf("%s\n",answer.c_str());
        long a = 0;
        for(int i=0; i<answer.size(); i++){
            a = (a * 10) + (answer[i]-'0');
            if(a>INT_MAX and sign==true){
                return INT_MAX;
            }else if(sign==false and (a*(-1)<INT_MIN)){
                return INT_MIN;
            }
        }
        if(sign==false){
            a *= -1;
        }
        return (int)a; 
    }
};