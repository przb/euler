import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

public class p011 {
    public static void main(String[] args) {
        try {
            File numberGridFile = new File("p11_number_grid.txt");
            Scanner myReader = new Scanner(numberGridFile);
            
            while (myReader.hasNextLine()) {
                String data = myReader.nextLine();
                System.out.println(data.split(" "));

                // int[] fileData = {Integer.parseInt(data.split(" "))};
                
                // System.out.println(fileData);

            }
            myReader.close();
        } catch (FileNotFoundException e) {
            System.out.println("Error");
            e.printStackTrace();

        }
    }
}