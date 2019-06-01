import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {

    public static void main(String[] args) {
        int[] sixDigits = new int[977];
        int count = 0;
        for (int i = 100; i < 1000; i++) {
            for (int j = 100; j < 1000; j++) {
                int num = i * j;
                if (num > 99999 && isPalindrome(num)) {
                    sixDigits[count] = num;
                    count++;
                }
            }
        }
        Scanner in = new Scanner(System.in);
        int t = in.nextInt();
        for(int a0 = 0; a0 < t; a0++){
            int n = in.nextInt();
            int highestPalindrome = -1;
            for (int i = 0; i < 977; i++) {
                if (sixDigits[i] > highestPalindrome && sixDigits[i] < n) {
                    highestPalindrome = sixDigits[i];
                }
            }
            System.out.println(highestPalindrome);
        }
    }

    private static boolean isPalindrome(int num) {
        for (int i = 5; i > 0; i -= 2) {
            int upper = (int)Math.pow(10, i);
            int left = num / upper;
            int right = num % 10;
            num = num % upper;
            num = num / 10;
            if (left != right) {
                return false;
            }
        }
        return true;
    }
}

