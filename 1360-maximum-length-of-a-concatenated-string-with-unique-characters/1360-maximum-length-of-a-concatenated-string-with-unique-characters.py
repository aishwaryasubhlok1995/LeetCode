from collections import Counter

class Solution:
    def maxLength(self, arr: list[str]) -> int:
        charSet = set()

        def overlap(charSet, s):
            seen = set()
            for c in s:
                if c in charSet or c in seen:
                    return True  # Duplicate found in existing set or within the string itself
                seen.add(c)
            return False  # No duplicates

        def backtrack(i):
            if i == len(arr):
                return len(charSet)

            res = 0
            if not overlap(charSet, arr[i]):
                for c in arr[i]:
                    charSet.add(c)
                res = backtrack(i + 1)
                for c in arr[i]:
                    charSet.remove(c)
            return max(res, backtrack(i + 1))  # Don't concatenate arr[i]

        return backtrack(0)
