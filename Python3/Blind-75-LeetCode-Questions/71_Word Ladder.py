# A transformation sequence from word beginWord to word endWord using a dictionary wordList is a sequence of words beginWord -> s1 -> s2 -> ... -> sk such that:

# Every adjacent pair of words differs by a single letter.
# Every si for 1 <= i <= k is in wordList. Note that beginWord does not need to be in wordList.
# sk == endWord
# Given two words, beginWord and endWord, and a dictionary wordList, return the number of words in the shortest transformation sequence from beginWord to endWord, or 0 if no such sequence exists.

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList or not wordList or not beginWord or not endWord:
            return 0
        
        # save all word by converted word X*X : e.g. h*t: hot, hit, hat...
        convert_dict = defaultdict(list)
        for word in wordList:
            for i in range(len(beginWord)):
                convert_dict[word[:i] + '*' + word[i+1:]].append(word)

        q = deque()
        visited = set()
        
        q.append((beginWord, 1))
        visited.add(beginWord)
        while (q):
            current_word, step = q.popleft()
            for i in range(len(beginWord)):
                # check current word in converted dict
                convert_word = current_word[:i] + '*' + current_word[i+1:]
                for word in convert_dict[convert_word]:
                    if word == endWord:
                        return step + 1
                    if word not in visited:
                        visited.add(word)
                        q.append((word, step + 1))
        return 0