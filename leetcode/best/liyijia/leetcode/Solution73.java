package best.liyijia.leetcode;

import java.util.HashSet;

import static best.liyijia.leetcode.MatrixUtils.printMatrix;

/**
 * Created: 2024/2/15
 * Author: Li Yijia
 * Description:
 */
public class Solution73 {
    public static void setZeroes(int[][] matrix) {
        mathod1(matrix);

    }

    private static void mathod2(int[][] matrix) {
    //     法二：

    }

    private static void mathod1(int[][] matrix) {
        // 法一：用set记录下 0 所在的行和列。两次遍历
        HashSet<Integer> row0 = new HashSet<Integer>();
        HashSet<Integer> col0 = new HashSet<Integer>();
        int m = matrix.length;
        int n = matrix[0].length;
        System.out.println("Before: ");
        printMatrix(matrix);
        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                if (matrix[i][j] == 0) {
                    row0.add(i);
                    col0.add(j);
                }
            }
        }
        System.out.println("row0 : " + row0);
        System.out.println("col0 : " + col0);

        for (int i = 0; i < m; ++i) {
            if (row0.contains(i)) {
                for (int j = 0; j < n; ++j) {
                    matrix[i][j] = 0;
                }
                continue;
            }

            for (int j = 0; j < n; ++j) {
                if (col0.contains(j)) {
                    matrix[i][j] = 0;
                }
            }
        }
        System.out.println("After: ");
        printMatrix(matrix);
    }

    public static void main(String[] args) {
        int[][] matrix = { {1,1,1},{1,0,1},{1,1,1}};
        int [][] matrix2 = { {0,1,2,0},{3,4,5,2},{1,3,1,5} };
        System.out.println("===matrix===");
        setZeroes(matrix);
        System.out.println("===matrix2===");
        setZeroes(matrix2);

    }



}
