import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int t = in.nextInt();
        for(int a0 = 0; a0 < t; a0++){
            long n = in.nextLong();
            long root = (long)Math.sqrt(n);
            long highestPrime = 0;
            long temp = n;
            while (n%2 == 0) {
                n /= 2;
                highestPrime = 2;
            }
            long count = 3;
            while (count <= temp/2 && count <= root) {
                if (n % count == 0) {
                    n /= count;
                    highestPrime = count;
                } else {
                    count += 2;
                }
            }
            if (n != 1) {
                highestPrime = n;
            }
            System.out.println(highestPrime);
        }
    }
}

