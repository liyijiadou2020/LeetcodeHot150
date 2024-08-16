from typing import List


def covered(a: List[int], b: List[int]):
    """
    判断两个区间是否存在重合。
    :param a:
    :param b:
    :return:
    """
    if b[0] > a[1]:
        return False
    if a[0] > b[1]:
        return False
    return True

def testCovered():
    print(covered([1, 3], [4, 6]))
    print(covered([4, 6], [1, 3]))
    print(covered([1, 3], [3, 6]))
    print(covered([1, 3], [1, 3]))
    print(covered([1, 3], [2, 4]))

def update(a: List[int], b: List[int]):
    """
    在保证a,b有交集的情况下，返回区间a和区间b的交集
    :param a:
    :param b:
    :return:
    """
    assert covered(a, b)
    left = max(a[0], b[0])
    right = min(a[1], b[1])
    return [left, right]

def testUpdate():
    # print(update([1, 3], [4, 6]))
    # print(update([4, 6], [1, 3]))
    print(update([1, 3], [3, 6]))
    print(update([1, 3], [1, 3]))
    print(update([1, 3], [2, 4]))

def findMinArrowShots(points: List[List[int]]) -> int:
    """
    452. 用最少数量的箭引爆气球
    :param points: [[10,16],[2,8],[1,6],[7,12]]
    :return: 2
    思路：先按照起始位置排序，遍历气球数组，每两个比较求解公共区间，
    若是有公共区间，用更新后的公共区间与下一个气球区间作比较，继续遍历，否则弓箭数加一
    """
    # 按照起始位置排序
    points.sort(key=lambda x: x[0])
    ans = 1
    interset = [points[0][0], points[0][1]]
    for point in points:
        if covered(interset, point):
            interset = update(interset, point)  # 更新交集
        else:
            ans += 1  # 弓箭数 += 1
            interset = point  # interset 更新为当前的区间

    return ans

def testFindMinArrowShots():
    points = [[10, 16], [2, 8], [1, 6], [7, 12]]
    assert findMinArrowShots(points) == 2

    points2 = [[1, 2], [3, 4], [5, 6], [7, 8]]
    assert findMinArrowShots(points2) == 4

    points3 = [[1, 2], [2, 3], [3, 4], [4, 5]]
    assert findMinArrowShots(points3) == 2