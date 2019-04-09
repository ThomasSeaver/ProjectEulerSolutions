import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int t = in.nextInt();
        long[] cache = new long[10001];
        cache[1] = 2;
        int count = 3;
        int high = 1;
        for(int a0 = 0; a0 < t; a0++){
            int n = in.nextInt();
            while (high < n) {
                if (isPrime(count)) {
                    high++;
                    cache[high] = count;
                }
                count++;
            }
            System.out.println(cache[n]);
        }
    }

    private static boolean isPrime(int num) {
        for (int i = 2; i <= num/2; i++) {
            if (num % i == 0) {
                return false;
            }
        }
        return true;
    }
}

