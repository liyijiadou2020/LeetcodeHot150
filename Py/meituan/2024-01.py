"""
@ File       : 2024-01.py
@ Time       ：2024/5/10
@ Author     ：Li Yijia
@ version    ：python 3.8.12
@ Description：美团2024年春招第一场笔试【测试方向】
"""


def count_perfect_rectangles(matrix):
    n = len(matrix)
    perfect_rectangles = [0] * (n + 1)

    # 计算每个位置作为矩形右下角时的完美矩形区域数量
    for i in range(n):
        for j in range(n):
            # 以位置 (i, j) 作为右下角的矩形的大小从1到n
            for k in range(1, min(n - i, n - j) + 1):
                # 计算当前矩形区域内0和1的数量
                zeros = ones = 0
                for x in range(i, i + k):
                    for y in range(j, j + k):
                        if matrix[x][y] == 0:
                            zeros += 1
                        else:
                            ones += 1
                # 如果0和1的数量相等，则该矩形区域是完美的
                if zeros == ones:
                    perfect_rectangles[k] += 1

    return perfect_rectangles


def demo01():
    """
    1.小美的平衡矩阵
        小美拿到了一个 n * n 的矩阵，其中每个元素是0或者1。
        小美认为一个矩形区域是完美的，当且仅当该区域内0的数量恰好等于1的数量。
        现在，小美希望你回答有多少个 i * i
        i∗i的完美矩形区域。你需要回答 i 属于 1≤i≤n的所有答案。

    :return:
    """
    # 读取输入
    n = int(input())
    matrix = [list(map(int, input().strip())) for _ in range(n)]

    # 计算每个i*i的完美矩形区域的数量并输出结果
    results = count_perfect_rectangles(matrix)
    for result in results[1:]:
        print(result)

demo01()

def demo02():
    """2.小美的数组询问"""
    n, q = map(int, input().split())
    nums = list(map(int, input().split()))
    base = 0
    delta_num = 0
    for x in nums:
        if x!=0:
            base += x
        else:
            delta_num += 1

    for _ in range(q):
        data = list(map(int, input().split()))
        l = data[0]
        r = data[1]
        min_res = base + l * delta_num
        max_res = base + r * delta_num
        print(min_res, ' ', max_res)

# ===================================================================


def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)


def is_valid_birthdate(birthdate):
    try:
        year = int(birthdate[:4])
        month = int(birthdate[4:6])
        day = int(birthdate[6:])

        if year < 1900 or year > 2023 or month < 1 or month > 12 or day < 1:
            return False

        if month in [1, 3, 5, 7, 8, 10, 12]:
            return day <= 31
        elif month in [4, 6, 9, 11]:
            return day <= 30
        elif month == 2:
            if is_leap_year(year):
                return day <= 29
            else:
                return day <= 28
    except ValueError:
        return False


def is_valid_group(group):
    return len(set(group)) == 3


def is_valid_checksum(employee_id, number):
    checksum = int(number[-1])
    digits = [int(digit) for digit in employee_id]
    if sum(digits) % 8 == 1:
        return True
    else:
        return False


def is_valid_employee_id(employee_id, birthdate, group, number):
    if not is_valid_birthdate(birthdate):
        return False
    if not is_valid_group(group):
        return False
    if not is_valid_checksum(employee_id, number):
        return False
    return True


def validate_employee_ids(departments, employee_ids):
    valid_departments = set(departments)
    results = []

    for employee_id in employee_ids:
        department, birthdate, group, number = employee_id[:6], employee_id[6:14], employee_id[14:17], employee_id[17:]
        if department not in valid_departments:
            results.append("error")
            continue

        if not is_valid_employee_id(employee_id, birthdate, group, number):
            results.append("error")
        else:
            results.append("ok")

    return results




def demo03():
    """
    3.验证工号
        假设美团的工号是由18位数字组成的，由以下规则组成：
        1. 前面6位代表是哪个部门
        2. 7-14位代表是出生日期，范围是1900.01.01-2023.12.31
        3. 15-17位代表是哪个组，不能是完全一样的3位数字
        4. 18位是一位的校验和，假设是x, 则需要满足(x+a1+a2+...a17) mod 8 = 1, a1..a17 代表了前面的17位数字

        现在需要写一份代码，判断输入的工号是否符合对应的规则。
        提示：出生日期这里需要判断闰年。闰年判断的条件是能被 4 整除， 但不能被 100 整除；或能被 400 整除。

        输入描述：
        第一行输入一个整数n (n 属于 [1,10])
        接下来n行，每行输入一个字符串，表示一个合法的部门。如果工号不属于合法部门的话，则认为这个工号不符合规则。
        接下来输入一个整数m (m 属于 [1,10])
        接下来m行，每行输入一个字符串，表示需要验证的工号。

        输出描述：
        如果不满足上述任一个规则，输出 "error" ，都满足的话输出 "ok"
    """
    n = int(input())
    valid_departments = [input().strip() for _ in range(n)]
    m = int(input())
    employee_ids = [input().strip() for _ in range(m)]

    # 验证工号并输出结果
    results = validate_employee_ids(valid_departments, employee_ids)
    for result in results:
        print(result)

