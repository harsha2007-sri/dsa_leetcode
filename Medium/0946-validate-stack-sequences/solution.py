class Solution(object):
    def validateStackSequences(self, pushed, popped):
        """
        :type pushed: List[int]
        :type popped: List[int]
        :rtype: bool
        """
        s=[]
        j=0
        for i in pushed:
            s.append(i)
            while s and s[-1]==popped[j]:
                s.pop()
                j+=1 
        return len(s)==0


        
