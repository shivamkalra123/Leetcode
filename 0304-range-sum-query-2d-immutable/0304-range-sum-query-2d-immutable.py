class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        rows, cols = len(matrix), len(matrix[0])
        self.prefix = [[0]*(cols+1) for _ in range(rows+1)]

        for r in range(1, rows+1):
            for c in range(1, cols+1):
                self.prefix[r][c] = (
                    matrix[r-1][c-1] +
                    self.prefix[r-1][c] +
                    self.prefix[r][c-1] -
                    self.prefix[r-1][c-1]
                )

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return (self.prefix[row2+1][col2+1]
               - self.prefix[row1][col2+1]
               - self.prefix[row2+1][col1]
               + self.prefix[row1][col1])
