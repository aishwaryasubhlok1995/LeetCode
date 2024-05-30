class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        i = 0
        j = len(matrix)-1
        while i<=j:
            mid = (i+j)//2
            if target>= matrix[mid][0] and target<= matrix[mid][-1]:
                start = 0
                end = len(matrix[0]) - 1
                while start<=end:
                    middle = (start+end)//2
                    print(start)
                    print(end)
                    print(middle)
                    if target == matrix[mid][middle]:
                        return True
                    if target < matrix[mid][middle]:
                        end = middle -1
                    elif target > matrix[mid][middle]:
                        start = middle +1
                return False
            elif target<matrix[mid][0]:
                j = mid-1
            elif target>matrix[mid][-1]:
                i = mid+1
        return False