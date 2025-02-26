class Solution:

    def preProcessing(self, wordsDict):
        hm = {}
        for i in range(len(wordsDict)):
            if wordsDict[i] not in hm:
                hm[wordsDict[i]] = []
            hm[wordsDict[i]].append(i) 
        return hm
    
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        minDistance = math.inf
        dictWords = self.preProcessing(wordsDict)
        array1 = dictWords[word1]
        array2 = dictWords[word2]
        i = 0 
        j = 0 
        while i<len(array1) and j<len(array2):
            minDistance = min(minDistance, (abs(array1[i]-array2[j])))
            if array1[i] < array2[j]:
                i += 1
            else:
                j += 1
        return  minDistance
        