# The count-and-say sequence is a sequence of digit strings defined by the recursive formula:

class Solution:        
    def countAndSay(self, n: int) -> str:
        if n < 2:
            return '1'
        
        # find the root str
        cur_str = self.countAndSay(n-1)
        answer, start, cnt = '', cur_str[0], 1
        for i in range(1, len(cur_str)):
            if cur_str[i] == start:
                cnt += 1
            else:
                answer += str(cnt) + start
                start = cur_str[i]
                cnt = 1
        answer += str(cnt) + start
        return answer