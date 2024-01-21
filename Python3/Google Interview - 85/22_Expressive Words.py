# Sometimes people repeat letters to represent extra feeling. For example:

# "hello" -> "heeellooo"
# "hi" -> "hiiii"
# In these strings like "heeellooo", we have groups of adjacent letters that are all the same: "h", "eee", "ll", "ooo".

# You are given a string s and an array of query strings words. A query word is stretchy if it can be made to be equal to s by any number of applications of the following extension operation: choose a group consisting of characters c, and add some number of characters c to the group so that the size of the group is three or more.

# For example, starting with "hello", we could do an extension on the group "o" to get "hellooo", but we cannot get "helloo" since the group "oo" has a size less than three. Also, we could do another extension like "ll" -> "lllll" to get "helllllooo". If s = "helllllooo", then the query word "hello" would be stretchy because of these two extension operations: query = "hello" -> "hellooo" -> "helllllooo" = s.
# Return the number of query strings that are stretchy.

class Solution:
    def expressiveWords(self, s: str, words: List[str]) -> int:
        def generateTable(s):
            if not s:
                return [], []

            chars, nums = [s[0]], [1]
            for i in range(1, len(s)):
                if s[i] == chars[-1]:
                    nums[-1] += 1
                else:
                    chars.append(s[i])
                    nums.append(1)
            return chars, nums

        answer = 0

        s_chars, s_nums = generateTable(s)
        for word in words:
            w_chars, w_nums = generateTable(word)

            if s_chars == w_chars:
                cnt = 0
                for i in range(len(w_chars)):
                    if (w_nums[i] == s_nums[i]) or (w_nums[i] < s_nums[i] and s_nums[i] >= 3):
                        cnt += 1

                if cnt == len(w_chars):
                    answer += 1
        return answer