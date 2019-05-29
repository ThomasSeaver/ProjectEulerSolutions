import java.io.*;
import java.util.*;

public class Solution {

    // create some arrays to keep track of steps taken from particular number
    // as well as which number has the most steps up to the given number
    static int[] listCheck = new int[5000001];
    static int[] bestNums = new int[5000002];

    public static void main(String[] args) {
        // Initiate base cases since we're using recursion
        listCheck[1] = 1;
        bestNums[1] = 1;
        int mostSteps = 0;
        int bestNum = 0;
        // Go from 2 to 5 million since these are the non trivial sequences
        // to check as laid out by question
        for (int i = 2; i < 5000001; i++) {
            // Propagate last chosen best number
            bestNums[i+1] = bestNums[i];
            // Check length of collatz number for current num
            // Subtract one because basecase of one actually has an extra step
            // Have to make basecase one because in truth it is 0 but arrays
            // initialize to zero and don't want to set whole thing
            int steps = findCollatz(i) - 1;
            // If our steps are higher then before, or our current sequence
            // is tied, then set a new best number/new step record
            if (steps > mostSteps || steps == mostSteps && bestNums[i] < bestNum) {
                mostSteps = steps;
                bestNum = i;
            }
            bestNums[i] = bestNum;
        }
        // Actually go through input and deal out answers
        // Faster to do all at once after primary calculations because
        // even using caching for all numbers means that for 1...10^4 inputs
        // we could count up to 5 million every time
        Scanner in = new Scanner(System.in);
        int num = in.nextInt();
        for (int j = 0; j < num; j++) {
            System.out.println(bestNums[in.nextInt()]);
        }
    }

    // Recursive function for finding and caching sequence steps
    public static int findCollatz(long num) {
        int result = 0;
        // If our number is not within our caching bounds or not cached
        if (num > 5000000 || listCheck[(int) num] == 0) {
            // Check if even
            if (num % 2 == 0) {
                // If even, add one step then check collatz sequence of
                // new number (n/2)
                result = 1 + findCollatz(num / 2);
            } else {
                // If odd, add one step then check collatz sequence of
                // new number (3n+1)
                result = 1 + findCollatz(3 * num + 1);
            }
            // after getting result, if number is cacheable
            if (num < 5000001) {
                // cache number
                listCheck[(int) num] = result;
            }
        } else {
            // if number is already pre-cached, pull it out
            result = listCheck[(int) num];
        }
        // return found number
        return result;
    }
}

