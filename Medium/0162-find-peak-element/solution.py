class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in range(len(nums)):
            if len(nums)==1:
                return 0
            if i==len(nums)-1:
                if nums[i]>nums[i-1]:
                    return i
            else:
                if nums[i]>nums[i+1] and nums[i]>nums[i-1]:
                    return i
