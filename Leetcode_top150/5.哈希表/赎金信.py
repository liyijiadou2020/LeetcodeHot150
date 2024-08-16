

"""
这段代码检查是否可以用magazine中的字符构成ransomNote。它使用了Python的collections.Counter类，这是一个用来计数的字典子类。以下是代码的逐步解释：

collections.Counter(ransomNote):

这个部分会创建一个Counter对象，其中包含ransomNote中每个字符的计数。例如，如果ransomNote是"aabb", 那么这个Counter对象会是{'a': 2, 'b': 2}。
collections.Counter(magazine):

类似地，这个部分会创建一个Counter对象，其中包含magazine中每个字符的计数。例如，如果magazine是"aabbbcc", 那么这个Counter对象会是{'a': 2, 'b': 3, 'c': 2}。
collections.Counter(ransomNote) - collections.Counter(magazine):

这个部分会计算两个Counter对象之间的差异，结果是一个新的Counter对象，表示ransomNote中的字符比magazine中多出来的部分。例如，如果ransomNote是"aabbc", 而magazine是"aabb", 那么结果会是{'c': 1}，因为ransomNote中比magazine多了一个'c'。
return not ...:

最后的return not会返回True或False。如果collections.Counter(ransomNote) - collections.Counter(magazine)结果为空Counter（即所有ransomNote中的字符都可以在magazine中找到，并且数量足够），则not操作会使其变为True，否则为False。
综上所述，这段代码检查是否可以用magazine中的字符构成ransomNote。如果可以，返回True；否则返回False。
"""
import collections


def canConstruct(ransomNote: str, magazine: str) -> bool:
    """
    383 赎金信
    :param ransomNote:
    :param magazine:
    :return:
    """
    #     方法一、字符统计
    #     只需要满足magazine中的每个英文字母的统计次数都大于等于ransomNote中相同字母的统计次数即可
    if len(ransomNote) > len(magazine):
        return False
    # 一定要掌握！！这个Counter对象实际上是一张hash表

    return not collections.Counter(ransomNote) - collections.Counter(magazine)




magazine = "aab"
ransomNote = "aa"
canConstruct(ransomNote, magazine)