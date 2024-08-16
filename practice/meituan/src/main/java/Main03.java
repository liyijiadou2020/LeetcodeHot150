import java.util.*;

public class Main03 {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String word = scanner.nextLine();
        int result = minOperations(word);
        System.out.println(result);
        scanner.close();
    }

    public static int minOperations(String word) {
        int upperCount = 0;
        int lowerCount = 0;

        // 统计大写字母和小写字母的数量
        for (char c : word.toCharArray()) {
            if (Character.isUpperCase(c)) {
                upperCount++;
            } else {
                lowerCount++;
            }
        }

        // 计算最少操作次数
        if (upperCount == word.length()) {
            // 单词全为大写
            return 0;
        } else if (lowerCount == word.length()) {
            // 单词全为小写
            return 0;
        } else if (Character.isUpperCase(word.charAt(0)) && upperCount == 1) {
            // 第一个字母大写，其余小写
            return 0;
        } else if (Character.isUpperCase(word.charAt(0))) {
            // 首字母大写，需将其他字符改成小写
            return lowerCount;
        } else {
            if(lowerCount > upperCount){
                return upperCount;
            }else{
                return lowerCount;
            }
            // 第一个字母小写，需将首字母改成大写，且将其他字符改成小写
        }
    }
}