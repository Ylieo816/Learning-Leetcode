class Solution {
public:
    int findKthLargest(vector<int>& nums, int k) {
        // answer1: sort
        sort(nums.begin(), nums.end());
        return nums[nums.size()-k];
        
        // answer2: priority queue
//         priority_queue<int> data;
//         int l = nums.size();
//         for(int i=0; i<l; ++i){
//             data.push(nums[i]);
//         }
        
//         int arr[l];
//         for(int i=0; i<l; ++i){
//             arr[i] = data.top();
//             data.pop();
//         }
//         return arr[k-1];
    }
};