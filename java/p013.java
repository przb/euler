import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

/**
 * Work out the first ten digits of the sum of the following one-hundred
 * 50-digit numbers. [In the text file]
 */

public class p013 {

    public static void main(String[] args) throws FileNotFoundException {
        File file = new File("text-files/p013_numbers.txt");
        Scanner scn = new Scanner(file);
        long[] numbers = new long[100];
        long total = 0;

        for (int i = 0; i < numbers.length; i++) {
            numbers[i] = Long.parseLong(scn.nextLine().substring(0, 14));
        }
        scn.close();

        for (long l : numbers) {
            total += l;
        }

        String totalString = "" + total;
        totalString = totalString.substring(0, 10);
        System.out.println(totalString);

    }
}