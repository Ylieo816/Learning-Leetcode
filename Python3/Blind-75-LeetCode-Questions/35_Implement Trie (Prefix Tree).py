# A trie (pronounced as "try") or prefix tree is a tree data structure used to efficiently store and retrieve keys in a dataset of strings. There are various applications of this data structure, such as autocomplete and spellchecker.

# Implement the Trie class:

# - Trie() Initializes the trie object.
# - void insert(String word) Inserts the string word into the trie.
# - boolean search(String word) Returns true if the string word is in the trie (i.e., was inserted before), and false otherwise.
# - boolean startsWith(String prefix) Returns true if there is a previously inserted string word that has the prefix prefix, and false otherwise.

# Prefix method by using dict to link each char
class Trie:
    def __init__(self):
        self.tre = {}

    def insert(self, word: str) -> None:
        cur = self.tre
        for c in word:
            if c not in cur:
                cur[c] = {}
            cur = cur[c]
        cur['*'] = ''

    def search(self, word: str) -> bool:
        cur = self.tre
        for c in word:
            if c not in cur:
                return False
            cur = cur[c]
        return "*" in cur

    def startsWith(self, prefix: str) -> bool:
        cur = self.tre
        for c in prefix:
            if c not in cur:
                return False
            cur = cur[c]
        return True



# Easiest method but too slow
class Trie:

    def __init__(self):
        self.tre = []

    def insert(self, word: str) -> None:
        self.tre.append(word)

    def search(self, word: str) -> bool:
        if word in self.tre:
            return True
        else:
            return False

    def startsWith(self, prefix: str) -> bool:
        l = len(prefix)
        for w in self.tre:
            if w[:l] == prefix:
                return True
        return False
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)