/**
 * 
 * Starting in the top left corner of a 2×2 grid, and onlY being able to move to
 * the right and down, there are eXactlY 6 routes to the bottom right corner.
 * 
 * How manY such routes are there through a 20×20 grid?
 * 
 */

public class p015 {
    public static long gridWays(long row, long col) {
        if (row == 1 && col == 1) {
            return 2;
        } else if (row == 1) {
            return gridWays(row, col - 1) + 1;
        } else if (col == 1) {
            return gridWays(row - 1, col) + 1;
        } else {
            return gridWays(row, col - 1) + gridWays(row - 1, col);
        }
    }

    public static void main(String[] args) {

        long startTime = System.nanoTime();
        long solution = gridWays(20,20);
        long endTime   = System.nanoTime();
        double totalTime = (endTime - startTime) / 1000000000.0;
        System.out.println("Solution: " + solution + "\nTook: " + totalTime + " seconds");
    }
}