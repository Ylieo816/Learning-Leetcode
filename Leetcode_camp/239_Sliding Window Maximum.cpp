class Solution {
public:
    vector<int> maxSlidingWindow(vector<int>& nums, int k) {
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
            if(i>=k-1){ //把值儲存起來
                answer.push_back(nums[q.front()]);
            }
        }
        return answer;
    }
};