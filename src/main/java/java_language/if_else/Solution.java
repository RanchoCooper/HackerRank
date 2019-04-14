package java_language.if_else;

import java.util.Scanner;

/**
 * @author rancho
 * @date 2019-04-14
 */
public class Solution {

    private static final Scanner SCANNER = new Scanner(System.in);
    private static final int TWO = 2;

    public static void main(String[] args) {
        int n = SCANNER.nextInt();
        SCANNER.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");
        if (n % TWO == 0) {
            if (2 <= n  && n <= 5) {
                System.out.println("Not Weird");
            } else if (6 <= n && n <= 20) {
                System.out.println("Weird");
            } else if (20 < n) {
                System.out.println("Not Weird");
            } else {
                System.out.println("Unknown");
            }

        } else {
            System.out.println("Weird");
        }

        SCANNER.close();
    }

}
