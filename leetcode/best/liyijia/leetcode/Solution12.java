package best.liyijia.leetcode;

import java.lang.management.PlatformLoggingMXBean;
import java.util.HashMap;

/**
 * Created: 2024/2/19
 * Author: Li Yijia
 * Description:
 *
 * 12. 整数转罗马数字
 * 中等
 * 相关标签
 * 相关企业
 * 罗马数字包含以下七种字符： I， V， X， L，C，D 和 M。
 *
 * 字符          数值
 * I             1
 * V             5
 * X             10
 * L             50
 * C             100
 * D             500
 * M             1000
 * 例如， 罗马数字 2 写做 II ，即为两个并列的 1。12 写做 XII ，即为 X + II 。 27 写做  XXVII, 即为 XX + V + II 。
 *
 * 通常情况下，罗马数字中小的数字在大的数字的右边。但也存在特例，例如 4 不写做 IIII，而是 IV。数字 1 在数字 5 的左边，所表示的数等于大数 5 减小数 1 得到的数值 4 。同样地，数字 9 表示为 IX。这个特殊的规则只适用于以下六种情况：
 *
 * I 可以放在 V (5) 和 X (10) 的左边，来表示 4 和 9。
 * X 可以放在 L (50) 和 C (100) 的左边，来表示 40 和 90。
 * C 可以放在 D (500) 和 M (1000) 的左边，来表示 400 和 900。
 * 给你一个整数，将其转为罗马数字。
 *
 *
 *
 * 示例 1:
 *
 * 输入: num = 3
 * 输出: "III"
 * 示例 2:
 *
 * 输入: num = 4
 * 输出: "IV"
 * 示例 3:
 *
 * 输入: num = 9
 * 输出: "IX"
 * 示例 4:
 *
 * 输入: num = 58
 * 输出: "LVIII"
 * 解释: L = 50, V = 5, III = 3.
 * 示例 5:
 *
 * 输入: num = 1994
 * 输出: "MCMXCIV"
 * 解释: M = 1000, CM = 900, XC = 90, IV = 4.
 *
 *
 * 提示：
 *
 * 1 <= num <= 3999
 *
 */
public class Solution12 {

    static public String intToRoman(int num) {
        // 法一：用4张哈希表记录整数字符与罗马数字的对应（大力出奇迹）
        HashMap<Character, String> map1 = new HashMap<Character, String>() {{
            put('0', "");
            put('1', "I");
            put('2', "II");
            put('3', "III");
            put('4', "IV");
            put('5', "V");
            put('6', "VI");
            put('7', "VII");
            put('8', "VIII");
            put('9', "IX");
        }};
        HashMap<Character, String> map2 = new HashMap<Character, String>() {{
            put('0', "");
            put('1', "X");
            put('2', "XX");
            put('3', "XXX");
            put('4', "XL");
            put('5', "L");
            put('6', "LX");
            put('7', "LXX");
            put('8', "LXXX");
            put('9', "XC");
        }};
        HashMap<Character, String> map3 = new HashMap<Character, String>() {{
            put('0', "");
            put('1', "C");
            put('2', "CC");
            put('3', "CCC");
            put('4', "CD");
            put('5', "D");
            put('6', "DC");
            put('7', "DCC");
            put('8', "DCCC");
            put('9', "CM");
        }};
        HashMap<Character, String> map4 = new HashMap<Character, String>(){{
            put('0', "");
            put('1', "M");
            put('2', "MM");
            put('3', "MMM");
        }};

        HashMap<Integer, HashMap<Character, String>> placeNumberMap = new HashMap<Integer, HashMap<Character, String>>() {{
            put(1, map1);
            put(2, map2);
            put(3, map3);
            put(4, map4);
        }};

        String numStr = String.valueOf(num);
        String res = "";
        System.out.println(numStr);
        int numStrLength = numStr.length();
        int place = 0;
        Character currentNumber = ' ';
        String tmpNumStr = "";
        for (int i = numStrLength - 1; i >= 0; --i) {
            place++; // 标记当前的符号是第几位
            currentNumber = numStr.charAt(i);
            HashMap<Character, String> characterStringHashMap = placeNumberMap.get(place);
            tmpNumStr = characterStringHashMap.get(currentNumber);
            // System.out.println("place: " + place + "currentNumber: " + currentNumber + " tmpNumStr: " + tmpNumStr);
            res = tmpNumStr + res;
        }
        System.out.println(res);
        return res;

    }

    static public String intToRoman2(int num) {
        // 法二【】题解：贪心算法我们每次尽量使用最大的数来表示。 比如对于 1994 这个数，如果我们每次尽量用最大的数来表示，依次选 1000，900，90，4，会得到正确结果 MCMXCIV。
        // 所以，我们将哈希表按照从大到小的顺序排列，然后遍历哈希表，直到表示完整个输入。
        StringBuffer res = new StringBuffer();

        Integer tmpInt = num;
        int[] value = new int[] {1000,900,500,400,100,90,50,40,10,9,5,4,1};
        String[] reps = new String[] {"M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"};
        int count = 0;
        for (int i = 0; i < value.length; i++) {
            while (num >= value[i]) {
                num -=  value[i];
                res.append(reps[i]);
            }
        }
        return res.toString();
    }



    public static void main(String[] args) {
        int num1 = 3;
        int num2 = 58;
        int num3 = 1994;
        int num4 = 3994;
        int num5 = 1;
        int num6 = 1000;
        int num7 = 10;
        int num8 = 3999;
        int num9 = 1010;
        String s1 = intToRoman(num1);
        String s2 = intToRoman(num2);
        String s3 = intToRoman(num3);
        String s4 = intToRoman(num4);
        String s5 = intToRoman(num5);
        String s6 = intToRoman(num6);
        String s7 = intToRoman(num7);
        String s8 = intToRoman(num8);
        String s9 = intToRoman(num9);
    }

}
