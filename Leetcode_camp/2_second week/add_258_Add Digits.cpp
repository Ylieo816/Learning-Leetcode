class Solution {
public:
    int addDigits(int num) {
        if(num<10){
            return num;
        }
        // while(num>=10){
        //     string data = to_string(num);
        //     int answer = 0;
        //     for(int i=0; i<data.size();++i){
        //         int v = data[i] - '0';
        //         answer += v;
        //     }
        //     num = answer;
        // }
        // return num;
        
        while(num>=10){
            int answer = 0;
            while(num>0){
            answer += num%10;
            num /=10;
            }
            num = answer;
        }
        return num;
    }
};