from typing import List


def hIndex(citations: List[int]) -> int:
    """
    274. H指数
    :param citations:
    :return:
    """
    n = len(citations)
    cnt = [0] * (n + 1)
    # 分析题目得知，h不可能超过论文总数n，因此对于引用次数大于n的论文，
    # 我们在统计时可以看成引用次数等于n的论文。
    for c in citations:
        cnt[min(c, n)] += 1 # 引用次数大于n的，等价于引用次数为n的
    s = 0 # 设s为引用次数 >= i的论文数，需算出满足s >= i的最大的i，因此倒序便利cnt
    for i in range(n, -1, -1):
        s += cnt[i]
        if s >= i:
            return i

print(hIndex([1,3,1]))