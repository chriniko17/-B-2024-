class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n=len(matrix)
        m=len(matrix[0])
        mark=False
        for i in range(n):
            if target<=matrix[i][m-1] and target>=matrix[i][0]:
                for j in range(m):
                    if matrix[i][j]>target:
                        break
                    elif matrix[i][j]==target:
                        mark=True
        return mark