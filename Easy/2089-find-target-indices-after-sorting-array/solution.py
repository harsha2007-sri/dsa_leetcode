class Solution(object):
    def targetIndices(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        def m_i_linear(arr,target):
            count=[]
            for _ in range(len(arr)):
                if arr[_]==target:
                    count.append(_)
            return count 
        return m_i_linear(sorted(nums),target)
