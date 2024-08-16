import java.util.Scanner;

public class Main01 {
    private static final int MOD = 1000000007;

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int q = sc.nextInt();
        long sum = 0;
        long[] a = new long[n];

        for (int i = 0; i < n; i++) {
            a[i] = sc.nextLong();
        }

        for (int i = 0; i < q; i++) {
            int x = sc.nextInt() - 1; // Convert to zero-based index
            for (int j = 0; j < n; j++) {
                if (j != x) {
                    a[j] *= 2;
                }
            }
            sum = ((sum - a[x] + MOD) % MOD * 2 % MOD + a[x]) % MOD;
        }

        System.out.println(sum);
        sc.close();
    }
}