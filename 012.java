import java.io.*;
import java.util.*;

public class Solution {

    // Arrays to store primes and results to prevent redoing work
    static int[] primes = primes(500000);
    static long[] results = new long[1001];

    public static void main(String[] args) {
        // Calculate which triangle numbers have which number of divisors
        int i = 0;
        long triangleDivisors = 0;
        for (int j = 1; j <= 1000; j++) {
            // go through every possible N
            while (triangleDivisors <= j) {
                // increment triangle number to dynamically calculate
                // through formula i * (i+1)/2
                i++;
                long countA = 0;
                long countB = 0;
                // Determine prime factors of i/2 and i+1 if i is even
                // or i+1/2 and i if i is odd, then multiply together
                // should be faster than counting prime factors of one number,
                // but I'm not entirely sure
                if (i % 2 == 0) {
                    countA = countPrimeFactors(i/2);
                    countB = countPrimeFactors(i+1);
                } else {
                    countA = countPrimeFactors(i);
                    countB = countPrimeFactors((i+1)/2);
                }
                triangleDivisors = countA*countB;
            }
            // store current triangle number as minimal triangle number for this
            // high of an N
            results[j] = (i*(i+1)/2);
        }

        // print out stored results
        Scanner in = new Scanner(System.in);
        int t = in.nextInt();
        for (int n = 0; n < t; n++) {
            int num = in.nextInt();
            System.out.println(results[num]);
        }
    }

    // Simple prime gathering method up to int limit. Output into array
    public static int[] primes(int limit) {
        int[] primes = new int[limit + 1];
        boolean[] isNotPrime = new boolean[limit + 1];
        // utilizing sieve of eratothenes
        int primeCount = 0;
        for (int i = 2; i <= limit; i++) {
            if(!isNotPrime[i]) {
                int count = i*2;
                while(count <= limit) {
                    isNotPrime[count] = true;
                    count += i;
                }
                primes[primeCount] = i;
                primeCount++;
            }
        }
        return primes;
    }

    // count prime factors of any particular number
    // this is useful because if a number is equal to (a^x)(b^y)(c^z)
    // we can find the number of divisors to be equal to (x+1)(y+1)(z+1)
    // this is through magic of primes and divisor stuff
    public static int countPrimeFactors(int num) {
        int triangleDivisors = 1;
        int divisor = 2;
        int curDivisor = 0;
        boolean usedDivisor = false;
        int primeCount = 0;
        while (num > 1) {
            if (num % divisor == 0) {
                if (!usedDivisor) {
                    usedDivisor = true;
                    curDivisor++;
                }
                curDivisor++;
                num /= divisor;
            } else {
                if (usedDivisor) {
                    triangleDivisors *= curDivisor;
                }
                divisor = primes[primeCount];
                primeCount++;
                usedDivisor = false;
                curDivisor = 0;
            }
        }
        if (usedDivisor) {
            triangleDivisors *= curDivisor;
        }
        return triangleDivisors;
    }
}

