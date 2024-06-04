class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rowList = []
        colmnList = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    rowList.append(i)
                    colmnList.append(j)
        for row in rowList:
            matrix[row] = [0] * len(matrix[0])
        for column in colmnList:
            for i in range(len(matrix)):
                matrix[i][column] = 0
        return matrix
                
        