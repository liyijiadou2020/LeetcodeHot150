import java.util.Scanner;
/**
 * Created with IntelliJ IDEA 2023.2.2
 *
 * @author Li Yijia
 * @date 2024/3/16
 */
public class Zhongshu_v3 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        int[] count = new int[3]; // 由于a_i只能为1或2，因此只需要两个位置

        for (int i = 0; i < n; i++) {
            int num = scanner.nextInt();
            count[num]++;
        }

        long sum = 0;
        for (int len = 1; len <= n; len++) { // 对于每个可能的区间长度
            for (int num = 1; num <= 2; num++) { // 分别计算1和2作为众数的情况
                if (count[num] >= (len + 1) / 2) { // 如果该数字出现次数足够多
                    long totalWays = Math.min(count[num], len - (len + 1) / 2 + 1);
                    sum += totalWays * num;
                }
            }
        }

        System.out.println(sum);
    }
}
