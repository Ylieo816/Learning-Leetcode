class Solution {
public:
    vector<int> maxSlidingWindow(vector<int>& nums, int k) {
//         #answer 1: deque
        deque<int> q;
        int l = nums.size();
        vector<int> answer;
        for(int i=0; i<l; ++i){
            if(!(q.empty()) && (q.front() == i-k)){ //丟掉前面的值
                q.pop_front();
            }
            
            while(!(q.empty()) && nums[i] > nums[q.back()]){ // 比較小就丟掉
                q.pop_back();
            }
            q.push_back(i);
            if(i>=k-1){
                answer.push_back(nums[q.front()]);
            }
        }
        return answer;
//      #answer 2: priority-queue !!!error answer, because priority_queue no remove!!
//         priority_queue<int> q;
//         int l = nums.size();
//         vector<int> answer;
//         for(int i=0; i<l; ++i){
//             int start = i-k;
//             if(start >=0){
//                 vector<int> save;
//                 while(q.top() != nums[start]){
//                     save.push_back(q.top());
//                     q.pop();
//                 }
//                 q.pop();
//                 for(int j=0; j<save.size(); ++j){
//                     q.push(save[j]);
//                 }
//             }
//             q.push(nums[i]);
//             if(q.size() == k){
//                 answer.push_back(q.top()); 
//             }
//         }
//         return answer;     
    }
};