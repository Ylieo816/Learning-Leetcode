class Solution {
public:
    vector<int> intersect(vector<int>& nums1, vector<int>& nums2) {
        // answer 1: double pointer
        sort(nums1.begin(), nums1.end());
        sort(nums2.begin(), nums2.end());
        vector<int> answer;
        int ptr1=0, ptr2=0;
        while(ptr1<nums1.size() && ptr2<nums2.size()){
            if(nums1[ptr1]>nums2[ptr2]){
                ptr2++;
            }else if(nums1[ptr1]<nums2[ptr2]){
                ptr1++;
            }else{
                answer.push_back(nums1[ptr1]);
                ptr1++;
                ptr2++;
            }
        }
        return answer;
        // answer2: map compare
        // int l1 = nums1.size(), l2 = nums2.size();
        // map<int, int> arr1, arr2;
        // vector<int> answer;
        // for(int i=0; i<l1; ++i){
        //     arr1[nums1[i]]++;
        // }
        // for(int i=0; i<l2; ++i){
        //     arr2[nums2[i]]++;
        // }
        // for(auto i: arr1){
        //     if(arr2[i.first]!=0){
        //         int m = min(i.second,arr2[i.first]);
        //         for(int j=0; j<m; ++j){
        //             answer.push_back(i.first);
        //         }
        //     }
        // }
        // sort(answer.begin(),answer.end());
        // return answer;
    }
};