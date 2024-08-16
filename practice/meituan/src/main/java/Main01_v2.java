import java.util.Scanner;
/**
 * Created with IntelliJ IDEA 2023.2.2
 *
 * @author Li Yijia
 * @date 2024/3/16
 */
public class Main01_v2 {
    public static void main(String[] args) {
        final int MOD = 1000000007;
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        int q = scanner.nextInt();
        long[] a = new long[n];
        long sum = 0;
        for (int i = 0; i < n; i++) {
            a[i] = scanner.nextLong();
            // sum = (sum + a[i]) % MOD;
            sum = sum + a[i];
        }

        long[] count = new long[n];
        for (int i = 0; i < q; i++) {
            int x = scanner.nextInt() - 1;
            count[x]++;
        }

        long totalSum = sum;
        for (int i = 0; i < n; i++) {
            long multiplier = (1L << q) - (1L << count[i]);
            multiplier %= MOD;
            totalSum = (totalSum + a[i] * multiplier) % MOD;
        }

        if (totalSum < 0) totalSum += MOD;
        System.out.println(totalSum);
    }
}
