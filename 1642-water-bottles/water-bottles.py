class Solution(object):
    def numWaterBottles(self, numBottles, numExchange):
        """
        :type numBottles: int
        :type numExchange: int
        :rtype: int
        """
        total = 0
        empty = 0

        while numBottles > 0:
            total += numBottles        # drink all full bottles
            empty += numBottles        # they become empty
            numBottles = empty // numExchange  # exchange empties for full
            empty = empty % numExchange         # keep leftover empties

        return total
