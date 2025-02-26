class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        minDistance = math.inf
        word1Idx = -1
        word2Idx = -1 
        for i in range(len(wordsDict)):
            if wordsDict[i] == word1:
                word1Idx = i 
            elif wordsDict[i] == word2:
                word2Idx = i 
            if (word1Idx != -1 and word2Idx != -1):
                minDistance= min(abs(word1Idx - word2Idx), minDistance)
        return  minDistance
        