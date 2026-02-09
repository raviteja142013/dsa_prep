class NumMatrix:

    def __init__(self, matrix: list[list[int]]):
        m = len(matrix)
        n= len(matrix[0])
        self.pref = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if i==0 and j==0:
                    self.pref[0][0] = matrix[0][0]
                elif i==0:
                    self.pref[i][j] = self.pref[i][j-1]+matrix[i][j]
                elif j==0:
                    self.pref[i][j] = self.pref[i-1][j]+matrix[i][j]
                else:
                    self.pref[i][j] = matrix[i][j]+self.pref[i-1][j]+self.pref[i][j-1]-self.pref[i-1][j-1]






    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        if row1==0:
             return self.pref[row2][col2]-self.pref[row2][col1-1]

        elif col1==0:
             return self.pref[row2][col2]-self.pref[row1-1][col2]

        else:

            return self.pref[row2][col2]-self.pref[row1-1][col2]-self.pref[row2][col1-1]+self.pref[row1-1][col1-1]


# Your NumMatrix object will be instantiated and called as such:
# matrix = [[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]]
# obj = NumMatrix(matrix)
# print(obj.pref)
# param_1 = obj.sumRegion(row1,col1,row2,col2)