import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

public class p013HundredDigitSum{

    
    public static void main(String[] args) throws FileNotFoundException {
        File file = new File("p013_numbers.txt");
        Scanner scn = new Scanner(file);
        long[] numbers = new long[100];
        long total = 0;

        for (int i = 0; i < numbers.length; i++){
            numbers[i] = Long.parseLong(scn.nextLine().substring(0,14));
        }
        scn.close();

        for (long l : numbers){
            total += l;
        }

        String totalString = "" + total;
        totalString = totalString.substring(0,10);
        System.out.println(totalString);
        
    }
}