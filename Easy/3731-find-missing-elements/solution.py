class Solution(object):
    def findMissingElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        a=min(nums)
        b=max(nums)
        ans=[]
        for i in range(a,b):
            if i not in nums:
                ans.append(i)
        return ans

        
