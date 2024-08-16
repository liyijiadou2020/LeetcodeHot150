package best.liyijia.leetcode;
import java.sql.SQLOutput;

/**
 * Created: 2024/2/15
 * Author: Li Yijia
 * Description: 14. 最长公共前缀 【Pass】
 *      编写一个函数来查找字符串数组中的最长公共前缀。
 *      如果不存在公共前缀，返回空字符串 ""。
 *      提示：
 *      - 1 <= strs.length <= 200
 *      - 0 <= strs[i].length <= 200
 *      - strs[i] 仅由小写英文字母组成
 */
public class Solution14 {

    static public String longestCommonPrefix(String[] strs) {
        String res = "";
        int n = strs.length;
        int maxLength = strs[0].length();
        // 找出res 的上限长度
        for (String str : strs) {
            if (str.length() < maxLength) {
                maxLength = str.length();
            }
        }
        if (maxLength == 0) {
            return res;
        }

        String prev = "";
        // 遍历所有的strs 找到最长公共前缀
        for (int i = 0; i < maxLength; ++i) {
            res += strs[0].charAt(i);
            for (String str : strs) {
                if (!str.startsWith(res)) {
                    return prev;
                }
            }
            prev = res;
        }
        return res;
    }

    public static void main(String[] args) {
        String[] strs =  { "flower","flow","flight" };
        System.out.println(longestCommonPrefix(strs));

        String[] strs2 =  { "flower","flow","flowght" };
        System.out.println(longestCommonPrefix(strs2));

        System.out.println(longestCommonPrefix(new String[] { "dog","racecar","car" }));

        System.out.println(longestCommonPrefix(new String[] { "","racecar","car" }));

        System.out.println(longestCommonPrefix(new String[] { "race","racecar","rade" }));




    }


}
