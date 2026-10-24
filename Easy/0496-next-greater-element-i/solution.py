class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        key=ele,value=next greater element
        """
        stack=[]
        d={}
        for n in nums2:
            while stack and n>stack[-1]:
                t=stack.pop()
                d[t]=n
            stack.append(n)
        while len(stack)!=0:
            t=stack.pop()
            d[t]=-1
        res=[]
        for n in nums1:
            res.append(d.get(n,-1))
        return res
