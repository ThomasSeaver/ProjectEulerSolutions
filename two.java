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
            long temp = -1;
            long fA = 1;
            long fB = 2;
            long sum = 0;
            while (fB < n) {
                if (fB % 2 == 0) {
                    sum += fB;
                }
                temp = fB;
                fB = fB + fA;
                fA = temp;
            }
            System.out.println(sum);
        }
    }
}

