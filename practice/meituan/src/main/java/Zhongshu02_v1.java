import java.util.*;
/**
 * Created with IntelliJ IDEA 2023.2.2
 *
 * @author Li Yijia
 * @date 2024/3/16
 */
public class Zhongshu02_v1 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        int[] arr = new int[n];
        for (int i = 0; i < n; i++) {
            arr[i] = scanner.nextInt();
        }
        int sum = 0;
        int[][] subArrays = getAllSubArrays(arr);
        for(int i = 0; i < subArrays.length; i++){
            sum += findMode(subArrays[i]);
        }
        System.out.println(sum);



    }
    public static int[][] getAllSubArrays(int[] nums) {
        List<int[]> subArrays = new ArrayList<>();
        for (int i = 0; i < nums.length; i++) {
            for (int j = i; j < nums.length; j++) {
                int[] subArray = new int[j - i + 1];
                for (int k = i; k <= j; k++) {
                    subArray[k - i] = nums[k];
                }
                subArrays.add(subArray);
            }
        }
        return subArrays.toArray(new int[subArrays.size()][]);
    }

    public static int findMode(int[] arr) {
        Map<Integer, Integer> countMap = new HashMap<>();

        int maxCount = 0;
        int mode = Integer.MAX_VALUE;
        for (int num : arr) {
            countMap.put(num, countMap.getOrDefault(num, 0) + 1);
            int count = countMap.get(num);

            if (count > maxCount || (count == maxCount && num < mode)) {
                maxCount = count;
                mode = num;
            }
        }

        return mode;
    }
}
