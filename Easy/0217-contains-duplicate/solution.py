class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        """ if len(nums)==len(set(nums)):
            return False
        else:
            return True"""
        count={}
        for i in nums:
            count[i]=count.get(i,0)+1
            if count[i]>1:
                return True
        return False
        
        count
