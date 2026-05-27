class Solution:
    def validWordSquare(self, words: List[str]) -> bool:
        for r, word in enumerate(words):
            for c, ch in enumerate(word):
                if c >= len(words) or r >= len(words[c]) or ch != words[c][r]:
                    return False
        return True