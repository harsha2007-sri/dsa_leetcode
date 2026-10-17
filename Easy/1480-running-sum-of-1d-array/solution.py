class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        num=0
        l=len(nums)
        arr=[0]*l
        for i in range(l):
            num+=nums[i]
            arr[i]=num
        return arr
