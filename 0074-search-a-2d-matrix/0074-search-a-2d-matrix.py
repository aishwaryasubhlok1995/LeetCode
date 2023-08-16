class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        low = 0
        high = len(matrix)-1
        while low <= high:
            middle = (low + high)//2 
            lowValue = matrix[middle][0]
            highValue = matrix[middle][-1]
            if target>= lowValue and target <= highValue:
                '''binary search for column'''
                start = 0
                end = len(matrix[middle])-1
                while(start<=end):
                    middlElement = (start+end)//2
                    if target == matrix[middle][middlElement]:
                        return True
                    elif target < matrix[middle][middlElement]:
                        end = middlElement - 1
                    elif target > matrix[middle][middlElement]:
                        start = middlElement + 1
                return False
            elif target< lowValue:
                high = middle - 1
            elif target> highValue:
                low = middle + 1