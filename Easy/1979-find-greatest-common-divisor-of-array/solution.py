class Solution(object):
    def findGCD(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        mx=max(nums)
        mn=min(nums)
        for i in range(mx,0,-1):
            if mx%i==0 and mn%i==0:
                return i
