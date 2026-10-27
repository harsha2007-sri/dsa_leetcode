class Solution(object):
    def createGrid(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: List[str]
        """
        grid=[]
        for i in range(m):
            row=[]
            for j in range(n):
                if i==m-1 or j==0:
                    row.append('.')
                else:
                    row.append('#')
            grid.append("".join(row))
        return grid
