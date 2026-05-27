class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        indexMap = {i:keyboard.index(i) for i in keyboard}
        timeTakenToType = 0 
        lastIndex = 0 
        for i in range(0, len(word)):
            timeTakenToType += abs(indexMap[word[i]] - lastIndex)
            lastIndex = indexMap[word[i]]

        return timeTakenToType


        