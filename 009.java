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
            // Keep track of A so that we keep highest minimal triple
            int maxA = -1;
            int n = in.nextInt();
            int result = -1;
            // Go through all triples using a generated formula in O(n)
            for (int b = 4; b < n/2; b++) {
                // We have two formulas, pythagorean
                // a^2 + b^2 = c^2
                // and known
                // a + b + c = n
                // so we find
                // c = n - a - b
                // Plug into pythagorean theorem, solve for a
                // Iterate over b, get all possible a's and c's,
                // verify that c is non negative (valid) and a is 
                // still highest a found, then check if pythagorean theorem
                // is still valid, and save result if so
                int a = ((n * n) - (2 * n * b))/((2 * n) - (2 * b)); 
                int c = n - a - b;
                if (c > 0 && a > maxA && b > a && a*a + b*b == c*c) {
                    maxA = a;
                    result = a*b*c;
                }
            }
            System.out.println(result);
        }
    }
}

