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
            int n = in.nextInt();
            int[] factors = new int[n + 1];
            for (int i = 2; i <= n; i++) {
                int check = i;
                int[] temp = new int[i/2 + 1];
                for (int j = 2; j <= i/2; j++) {
                    if (check % j == 0) {
                        check /= j;
                        temp[j]++;
                        j--;
                    }
                }
                if (check == i) {
                    factors[i]++;
                } else {
                    for (int j = 2; j < temp.length; j++) {
                        if (temp[j] > factors[j]) {
                            factors[j] = temp[j];
                        }
                    }
                }
            }
            int total = 1;
            for (int i = 2; i < factors.length; i++) {
                int exp = (int)Math.pow(i, factors[i]);
                total *= exp;
            }
            System.out.println(total);
        }
    }
}

