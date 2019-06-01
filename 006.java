import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int t = in.nextInt();
        long highestCalc = 1;
        long[] cache = new long[10001];
        for(int a0 = 0; a0 < t; a0++){
            int n = in.nextInt();
            long sum = 0;
            // If we've already calculated/cached answer, just serve it up
            if (highestCalc > n) {
                sum = cache[n];
            } else {
                // If we have calculated before, get highest calculation
                // to avoid repeating our work
                if (highestCalc > 1) {
                    sum = cache[(int)highestCalc];
                }
                // Formula is (1 + 2 + ... + n)^2 - (1^2 + 2^2 + ... + n^2)
                // Works out to (1^2 + 2^2 + ... + n^2 + 2(1 * 2) + 2(1 * 3) + 2(2 * 3)
                // + ... + 2((n-2) * n) + 2((n-1) * n)) - (1^2 + 2^2 + ... + n^2)
                // This way because of binomial expansions, just cut out squares
                // for func(n), answer is 2*(func(n-1) + sum ([i up to n-1] * n))
                for (long i = highestCalc + 1; i <= n; i++) {
                    for (long j = 1; j < i; j++) {
                        sum += j*i;
                    }
                }
            }
            // cache prev answers to avoid repeating work, multiply sum by 2
            // as in binomial expansions, and update our highest calc before printing out
            cache[n] = sum;
            sum *= 2;
            highestCalc = (long)n;
            System.out.println(sum);
        }
    }
}

