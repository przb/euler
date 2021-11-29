/*
2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2^1000?
*/

import java.util.ArrayList;

public class p016 {
    public final static int DECIMAL = 10;

    /**
     * Doubles the element i. If the doubled number needs to carry, then it carries
     * over. If the carried number
     * increases the length of the digit, returns true.
     * 
     * @param arr ArrayList which treats element with index n, as the 10^(arr.size -
     *            n - 1) position
     * @param i   the index of the number that you are doubling
     * @return true if number was added, false otherwise. Changes the value of the
     *         indexes either way.
     */
    public static boolean doubleElement(ArrayList<Integer> arr, int i) {

        // Calling the digits 10s and 1s digit is a little erroneous, as the variables
        // could be
        // any place holder, not just tens and ones. A more apt name would be carried
        // value, and remainder value.
        int nextElement = arr.get(i) * 2;
        int tensDigit = nextElement / DECIMAL;
        int onesDigit = nextElement % DECIMAL;

        // If there is no carry, just doubles the ones digit.
        if (tensDigit == 0) {
            arr.set(i, onesDigit);
        }

        // If there is a carry and the index is 0, then makes the arraylist longer and
        // adds the
        // tens digit to the beginning of the array, and returns true.
        else if (i == 0) {
            arr.set(i, onesDigit);
            arr.add(0, tensDigit);
            return true;
        }

        // IF there is a carry, then it adds the value of the tens digit to the digit
        // where
        // the tens value is stored.
        else {
            arr.set(i, onesDigit);
            arr.set(i - 1, tensDigit + arr.get(i - 1));
        }
        return false;
    }

    /**
     * Takes an arraylist of intigers and treats it as one intiger with all elements
     * concatentated together.
     * Then doubles the number resulting from the concatentation.
     * 
     * @param arr ArrayList which treats element with index n, as the 10^(arr.size -
     *            n - 1) position
     */
    public static void powerTwo(ArrayList<Integer> arr) {
        for (int i = 0; i < arr.size(); i++) {
            if (doubleElement(arr, i)) {
                i++;
            }
        }
    }

    public static void main(String[] args) {
        ArrayList<Integer> powersOfTwoDigits = new ArrayList<Integer>();
        powersOfTwoDigits.add(2);

        // This loops first iteration starts it at 2^2, so it only goes until 999
        for (int i = 0; i < 999; i++) {
            powerTwo(powersOfTwoDigits);
        }

        // Sums all the items in the arraylist
        int total = 0;
        for (int n : powersOfTwoDigits) {
            total += n;
        }
        System.out.println("total: " + total + "\ndigits in sum: " + powersOfTwoDigits.size());
    }
}