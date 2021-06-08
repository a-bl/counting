# Counting islands

import random


class Solution(object):
    def num_islands(self, grid):
        if len(grid) == 0:
            return 0
        n = len(grid)
        m = len(grid[0])
        ans = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    ans += 1
                self.make_water(i, j, n, m, grid)
        return ans

    def make_water(self, i, j, n, m, grid):
        if i < 0 or j < 0 or i >= n or j >= m:
            return
        if grid[i][j] == 0:
            return
        else:
            grid[i][j] = 0
        self.make_water(i + 1, j, n, m, grid)
        self.make_water(i, j + 1, n, m, grid)
        self.make_water(i - 1, j, n, m, grid)
        self.make_water(i, j - 1, n, m, grid)


def get_matrix(row, col):
    matrix = [[random.randrange(0, 2) for y in range(col)] for x in range(row)]
    for im in range(row):
        print(matrix[im])
    return matrix


if __name__ == '__main__':
    row = int(input('Enter a number of rows:'))
    col = int(input('Enter a number of columns:'))
    obj = Solution()
    print(obj.num_islands(get_matrix(row, col)))

