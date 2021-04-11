class Solution {
public:
    vector<int> relativeSortArray(vector<int>& arr1, vector<int>& arr2) {
        map<int,int> table1;
        int l1 = arr1.size();
        int l2 = arr2.size();
        // vector<int> answer;
        for(int i=0; i<l1; i++){
            table1[arr1[i]]++;
        }
        int index=0;
        for(int i=0; i<l2;i++){
            int s = table1[arr2[i]];
            for(int j=0; j<s; index++,j++){
                arr1[index] = arr2[i];
                table1[arr2[i]]--;
            }
        }
        for(auto data:table1){
            for(int i = 0; i<data.second; index++,i++){
                arr1[index] = data.first;
            }
        }
        return arr1;
    }
};