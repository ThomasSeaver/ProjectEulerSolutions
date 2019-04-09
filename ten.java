import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {

    public static void main(String[] args) {
        int limit = 1000000;
        long[] cache = new long[limit + 1];
        boolean[] isNotPrime = new boolean[limit + 1];
        // utilizing sieve of eratothenes
        long sum = 0;
        for (int i = 2; i <= limit; i++) {
            if(!isNotPrime[i]) {
                sum += i;
                int count = i*2;
                while(count <= limit) {
                    isNotPrime[count] = true;
                    count += i;
                }
            }
            cache[i] = sum;
        }
        Scanner in = new Scanner(System.in);
        int t = in.nextInt();
        for(int a0 = 0; a0 < t; a0++){
            int n = in.nextInt();
            System.out.println(cache[n]);
        }
    }
}

