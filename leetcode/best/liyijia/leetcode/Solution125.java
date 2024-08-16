package best.liyijia.leetcode;

/**
 * Created: 2024/2/24
 * Author: Li Yijia
 * Description:
 */
public class Solution125 {

    static public boolean isPalindrome(String s) {
        if (s.length() <= 1) {
            return true;
        }

        // 去除非字母数字字符，大写转成小写，找到中间位置
        String afterReplaceString = s.trim().toLowerCase();
        System.out.println(afterReplaceString);
        int i = 0;
        int j = afterReplaceString.length() - 1;
        Character left;
        Character right;
        while (i <= j) {
            left = afterReplaceString.charAt(i);
            right = afterReplaceString.charAt(j);
            if (!Character.isLetterOrDigit(left)) {
                i++;
                continue;
            }
            if (!Character.isLetterOrDigit(right)) {
                j--;
                continue;
            }
            if (left.equals(right)) {
                i++;
                j--;
            } else {
                return false;
            }
        }
        return true;
    }

    public static void main(String[] args) {
        System.out.println(isPalindrome("A man, a plan, a canal: Panama"));
        System.out.println(isPalindrome("A man, a plan, a canal: h Panama"));
        System.out.println(isPalindrome("A ,,,,, b*%$^#$%^j       b     a"));
        System.out.println(isPalindrome("race a car"));
        System.out.println(isPalindrome(" "));

    }

}
