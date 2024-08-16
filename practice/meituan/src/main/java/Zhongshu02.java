import java.util.Scanner;
/**
 * Created with IntelliJ IDEA 2023.2.2
 *
 * @author Li Yijia
 * @date 2024/3/16
 */
public class Zhongshu02 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // Read the size of the array
        int n = scanner.nextInt();

        // Read the array elements
        int[] arr = new int[n];
        int[] count1 = new int[n];
        int[] count2 = new int[n];

        for (int i = 0; i < n; i++) {
            arr[i] = scanner.nextInt();
            // Populate the prefix sums for 1s and 2s
            count1[i] = (i > 0 ? count1[i - 1] : 0) + (arr[i] == 1 ? 1 : 0);
            count2[i] = (i > 0 ? count2[i - 1] : 0) + (arr[i] == 2 ? 1 : 0);
        }

        long sumOfModes = 0;

        // Find the mode for each subarray
        for (int start = 0; start < n; start++) {
            for (int end = start; end < n; end++) {
                int ones = count1[end] - (start > 0 ? count1[start - 1] : 0);
                int twos = count2[end] - (start > 0 ? count2[start - 1] : 0);
                // Add the mode of the subarray
                sumOfModes += (ones >= twos ? 1 : 2);
            }
        }

        System.out.println(sumOfModes);

        scanner.close();
    }
}
