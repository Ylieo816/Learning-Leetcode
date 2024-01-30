# Given a string paragraph and a string array of the banned words banned, return the most frequent word that is not banned. It is guaranteed there is at least one word that is not banned, and that the answer is unique.

# The words in paragraph are case-insensitive and the answer should be returned in lowercase.

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        paragraph = paragraph.lower()
        symbol = "!?',;."
        for s in symbol:
            paragraph = paragraph.replace(s, " ")
        paragraph = paragraph.split()
        table = Counter(paragraph)
        
        for ban in banned:
            if ban in table:
                del table[ban]
        
        return max(table, key=table.get)