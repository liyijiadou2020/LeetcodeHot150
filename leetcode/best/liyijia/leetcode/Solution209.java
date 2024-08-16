package best.liyijia.leetcode;
/**
 * Created with IntelliJ IDEA 2023.2.2
 *
 * @author Li Yijia
 * @date 2024/3/14
 * 力扣刷题：209. 长度最小的子数组
 * 给定一个含有 n 个正整数的数组和一个正整数 target 。
 * 找出该数组中满足其总和大于等于 target 的长度最小的 连续子数组
 *  [numsl, numsl+1, ..., numsr-1, numsr] ，并返回其长度。如果不存在符合条件的子数组，返回 0 。
 *
 * 示例 1：
 * 输入：target = 7, nums = [2,3,1,2,4,3]
 * 输出：2
 * 解释：子数组 [4,3] 是该条件下的长度最小的子数组。
 *
 * 示例 2：
 * 输入：target = 4, nums = [1,4,4]
 * 输出：1
 */
public class Solution209 {
    public static int minSubArrayLen(int target, int[] nums) {
        int res = 0;

        return res;
    }

    public static void main(String[] args) {
        System.out.println(minSubArrayLen(7, new int [] {2,3,1,2,4,3}));

    }
}
