class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False]*(len(s) + 1)
        dp[-1] = True
        for i in range(len(s)-1, -1, -1):
            for word in wordDict:
                if len(s[i::]) < len(word):
                    continue
                else:
                    if s[i:i+len(word)] == word:
                        if dp[i] == False:
                            dp[i] = dp[i + len(word)]
        return dp[0]

