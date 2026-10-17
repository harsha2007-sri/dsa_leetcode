class Solution(object):
    def heightChecker(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        hts = sorted(heights)
        j=c=0
        for i in heights:
            if i!=hts[j]:
                c+=1
            j+=1
        return c
