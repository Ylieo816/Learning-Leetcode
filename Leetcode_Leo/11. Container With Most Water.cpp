class Solution {
public:
    int maxArea(vector<int>& height) {
        int left = 0;
        int right = height.size()-1;
        int answer = 0;
        int area = 0;
        while(left < right){
            if (height[left] < height[right]){
                area = height[left] * (right-left);
                left++;
            }else{
                area = height[right] * (right-left);
                right--;
            }
            answer = max(area, answer);
        }
        return answer;
    }
};