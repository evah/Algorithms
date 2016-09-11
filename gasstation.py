# http://www.cnblogs.com/zuoyuan/p/3761023.html


class Solution:
    # @param gas, a list of integers
    # @param cost, a list of integers
    # @return an integer

    def canCompleteCircuit(self, gas, cost):
        if sum(gas) < sum(cost):
            return -1
        n = len(gas)
        diff = 0
        stationIndex = 0
        for i in range(n):
            if gas[i] + diff < cost[i]:
                stationIndex = i + 1
                diff = 0
            else:
                diff += gas[i] - cost[i]
        return stationIndex
