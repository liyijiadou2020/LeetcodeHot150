import collections
from typing import List


def groupAnagrams(strs: List[str]) -> List[List[str]]:
    """
    49. 字母异位词分组
    :param strs:
    :return:
    """
    # 语法？
    mp = collections.defaultdict(list)

    for st in strs:
        key = "".join(sorted(st))
        mp[key].append(st)

    return list(mp.values())

