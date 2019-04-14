package java_language.stdin_and_stdout_2;

import java.util.Scanner;

/**
 * @author rancho
 * @date 2019-04-14
 */
public class Solution {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int i = scanner.nextInt();
        double d = scanner.nextDouble();

        // 处理遗留的换行符
        scanner.nextLine();
        String s = scanner.nextLine();

        System.out.println("String: " + s);
        System.out.println("Double: " + d);
        System.out.println("Int: " + i);
    }

}
