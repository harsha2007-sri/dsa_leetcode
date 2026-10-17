class Solution(object):
    def shiftGrid(self, grid, k):
        """
        :type grid: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        rows = len(grid)
        cols = len(grid[0])

        while k > 0:
            # Save the last element
            last = grid[rows - 1][cols - 1]

            # Move elements one step to the right
            for i in range(rows - 1, -1, -1):
                for j in range(cols - 1, -1, -1):
                    if i == 0 and j == 0:
                        grid[i][j] = last
                    elif j == 0:
                        grid[i][j] = grid[i - 1][cols - 1]
                    else:
                        grid[i][j] = grid[i][j - 1]

            k = k - 1

        return grid
