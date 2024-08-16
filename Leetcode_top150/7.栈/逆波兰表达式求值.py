from typing import List


def evalRPN(tokens: List[str]) -> int:
    """
    150. 逆波兰表达式求值
    :param tokens: ["4","13","5","/","+"]
    :return: 6
    解释：该算式转化为常见的中缀算术表达式为：(4 + (13 / 5)) = 6

    思路：
    1. 维护一个栈，里面只存放数字
    2. 从头到尾遍历数组，只要遇到数字就压栈
    3. 重点来了。
        遇到了运算符就出栈两个数字。先出栈的是op1，后出栈的是op2。进行op1 _ op2 的运算，把得到的运算结果再入栈
    4. 对列表每个元素都进行如此操作，直到最后一个运算结束。此时栈内应该只剩一个数字，这个数就是最终运算结果
    """
    stack = list()
    for token in tokens:
        if token.lstrip('-').isdigit():
            stack.append(int(token))
        elif token == '+' and stack:
            op2 = stack.pop()
            op1 = stack.pop()
            res = op1 + op2
            stack.append(res)
        elif token == '-' and stack:
            op2 = stack.pop()
            op1 = stack.pop()
            res = op1 - op2
            stack.append(res)
        elif token == '*' and stack:
            op2 = stack.pop()
            op1 = stack.pop()
            res = op1 * op2
            stack.append(res)
        elif token == '/' and stack:
            op2 = stack.pop()
            op1 = stack.pop()
            res = int(op1 / op2)
            stack.append(res)
    return stack.pop()


# tokens = ["4", "13", "5", "/", "+"]
tokens = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
# tokens = ["2", "1", "+", "3", "*"]
print(evalRPN(tokens))


