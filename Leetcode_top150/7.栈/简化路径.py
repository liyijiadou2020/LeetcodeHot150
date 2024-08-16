import re


def simplifyPath(path: str) -> str:
    """
    71. 简化路径
    :param path: path = "/home/"
    :return: "/home"
    解释：注意，最后一个目录名后面没有斜杠。
    思路：
    1. 首先将给定的字符串 path 根据/分割成一个由若干字符串组成的列表，纪委names
    2. names中包含的字符串只能是以下几种情况：
        - 空串
        - 一个点.
        - 两个点 ..
        - 只包含英文字母、数字或_的目录名
    3. 空串和一个点.无意义。对于两个点..我们可以将目录名出栈；
        当我们遇到目录名则入栈
    4. 我们只需要遍历 names 中的每个字符串进行上述操作即可。在所有操作完成后，我们将
        从栈底到栈顶的字符串用/连接，再在最前面加上/表示根目录，就可以得到简化后的规范路径了。
    """
    names = path.strip().split('/')
    print(names)
    stack = list()
    for name in names:
        if name == "..":
            if stack:
                stack.pop()
        elif name and name != '.':
            stack.append(name)
    return '/' + '/'.join(stack)




# path = "/home//foo/"
path = "   /a//.//b//../../c/   "
print(simplifyPath(path))

