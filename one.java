import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int t = in.nextInt();
        int[] ar = new int[t];
        for(int a0 = 0; a0 < t; a0++){
            int n = in.nextInt();
            n--;
            int threes = 3*(n/3)*(n/3 + 1)/2;
            int fives = 5*(n/5)*(n/5 + 1)/2;
            int fifteens = 15*(n/15)*(n/15 + 1)/2;
            int count = threes + fives - fifteens;
            System.out.println(count);
        }
        in.close();
    }
}

