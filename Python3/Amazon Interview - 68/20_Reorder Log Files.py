# You are given an array of logs. Each log is a space-delimited string of words, where the first word is the identifier.

# There are two types of logs:

# Letter-logs: All words (except the identifier) consist of lowercase English letters.
# Digit-logs: All words (except the identifier) consist of digits.
# Reorder these logs so that:

# The letter-logs come before all digit-logs.
# The letter-logs are sorted lexicographically by their contents. If their contents are the same, then sort them lexicographically by their identifiers.
# The digit-logs maintain their relative ordering.
# Return the final order of the logs.

# # Time Complexity: O(M⋅N⋅log⁡N), N be the number of logs, M be the maximum length, sorted: log⁡N
# # Space Complexity: O(M⋅N)
class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        def get_key(log):
            # max split one time to get "identifier" and rest of body
            idx, body = log.split(" ", maxsplit = 1)
            # if this is letter sentence, return 0 with body for ranking
            if body[0].isalpha():
                return (0, body, idx)
            # else this is number sentence, return 1 with no body because keep origin order
            else:
                return (1,)

        # sort the log by (identifier, body, idx)
        return sorted(logs, key = get_key)

# append then sort by lambda
class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letters, digits = [], []

        for log in logs:
            if log.split()[1].isdigit():
                digits.append(log)
            else:
                letters.append(log)

        letters.sort(key=lambda x: (x.split()[1:], x.split()[0]))
        return letters + digits
        