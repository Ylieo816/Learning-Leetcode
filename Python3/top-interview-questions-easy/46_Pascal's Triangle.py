# Given an integer numRows, return the first numRows of Pascal's triangle.

# In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

# start with 2
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1: return [[1]]
        elif numRows == 2: return [[1], [1,1]]
        answer = [[1], [1,1]]
        for i in range(2, numRows):
            temp = [1]
            for j in range(len(answer[-1]) - 1):
                temp.append(answer[-1][j] + answer[-1][1+j])
            temp.append(1)
            answer.append(temp)
        return answer

# insert head and last to 0
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        answer = [[1]]
        
        for i in range(1, numRows):
            temp = [0] + answer[-1] + [0]
            next_temp = []
            for j in range(len(temp) -1 ):
                next_temp.append(temp[j] + temp[j+1])
            answer.append(next_temp)
        return answer