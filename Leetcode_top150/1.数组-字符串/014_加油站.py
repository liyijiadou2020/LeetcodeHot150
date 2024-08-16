from typing import List


def canCompleteCircuit(gas: List[int], cost: List[int]) -> int:
    """
    134. 加油站
    结论：如果X到不了Y，则X到达Y中间的任何一点时所剩的油箱容量都>=0，
    而从中间任何一点开始时的默认油量都 == 0，
    因此中间任何一点都不可能到达X到不了的Y
    :param gas:
    :param cost:
    :return:
    """
    n = len(gas)
    sum = 0
    for i in range(n):
        sum += gas[i] - cost[i]
    if sum < 0:
        return -1
    # 记录油箱中的油量
    tank = 0
    # 记录开始的位置
    start = 0
    for i in range(n):
        tank += gas[i] - cost[i]
        # 贪心算法：如果i到j恰好油量为负数，那么i~j之间的任一个站点都不可能作为起点
        if tank < 0:
            start = i + 1
            tank = 0
    return 0 if start == n else start


gas = [2, 3, 4]
cost = [3, 4, 3]
n = canCompleteCircuit(gas, cost)
print(n)
