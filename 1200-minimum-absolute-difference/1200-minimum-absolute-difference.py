
class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr = sorted(arr)
        ans = []
        minDiff = math.inf 
        for i in range(1, len(arr)):
            if arr[i] - arr[i-1] < minDiff:
                minDiff = arr[i] - arr[i-1]
                ans = [[arr[i-1], arr[i]]]
            elif arr[i] - arr[i-1] == minDiff:
                ans.append([arr[i-1], arr[i]])
        return ans 
            