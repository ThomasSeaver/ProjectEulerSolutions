import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int t = in.nextInt();
        int maxProduct = 0;
        for(int a0 = 0; a0 < t; a0++){
            maxProduct = 0;
            int n = in.nextInt();
            int k = in.nextInt();
            String num = in.next();
            for (int i = 0; i < n-k+1; i++) {
                String substr = num.substring(i, i+k);
                int product = productify(substr);
                if (product > maxProduct) {
                    maxProduct = product;
                }
            }
            System.out.println(maxProduct);
        }
    }

    public static int productify(String num) {
        int product = 1;
        int len = num.length();
        for (int i = 1; i <= len; i++) {
            product *= Character.getNumericValue(num.charAt(0));
            num = num.substring(1);
        }
        return product;
    }
}

