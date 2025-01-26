class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        start = 0
        end = len(matrix) - 1
        while start <= end:
            middle = (start + end)//2
            if target <= matrix[middle][-1] and target >= matrix[middle][0]:
                left = 0
                right = len(matrix[0]) - 1
                while left <= right:
                    mid = (left+right)//2
                    if matrix[middle][mid] == target:
                        return True
                    elif target < matrix[middle][mid]:
                        right = mid -1 
                    elif  target > matrix[middle][mid]:
                        left = mid +  1
                return False
            if target < matrix[middle][0]:
                end = middle - 1
            elif target > matrix[middle][-1]:
                start = middle + 1
        return False 




        