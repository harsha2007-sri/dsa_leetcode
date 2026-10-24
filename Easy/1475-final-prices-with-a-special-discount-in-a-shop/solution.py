class Solution(object):
    def finalPrices(self, prices):
        """
        :type prices: List[int]
        :rtype: List[int]
        """
        dis=[]
        for i in range(len(prices)):
            for j in range(len(prices)):
                if j>i and prices[j]<=prices[i]:
                    dis.append(prices[i]-prices[j])
                    break
            else:
                dis.append(prices[i])
        return dis

