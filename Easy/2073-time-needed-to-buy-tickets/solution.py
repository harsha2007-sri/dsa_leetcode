class Solution(object):
    def timeRequiredToBuy(self, tickets, k):
        """
        :type tickets: List[int]
        :type k: int
        :rtype: int
        """
        t=0
        while tickets[k]:
            for i in range(len(tickets)):
                if tickets[i]>0:
                    tickets[i]-=1
                    t+=1
                if tickets[k]==0:
                    return t
