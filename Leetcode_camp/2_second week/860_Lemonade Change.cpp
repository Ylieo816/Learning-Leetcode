class Solution {
public:
    bool lemonadeChange(vector<int>& bills) {
        int map[2] = {0};
        for(int i=0; i<bills.size();++i){
            if(bills[i]==5){
                map[0]++;
            }else if(bills[i]==10){
                if(map[0]>0){
                    map[0]--;
                    map[1]++;
                }else{
                    return false;
                }
            }else if(bills[i]==20){
                if(map[1]>0 and map[0]>0){
                    map[1]--;
                    map[0]--;
                }else if (map[0]>2){
                    map[0] -= 3;
                }else{
                    return false;
                }
            }
        }
        return true;
    }
};