package best.liyijia.leetcode;

/**
 * Created: 2024/2/15
 * Author: Li Yijia
 * Description:
 */
public class MatrixUtils {
    static void printMatrix(int[][] matrix) {
        int m = matrix.length;
        int n = matrix[0].length;

        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                System.out.print(matrix[i][j] + " ");
            }
            System.out.println();
        }

    }
}
