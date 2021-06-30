/*
If we list all the natural numbers below 10 
that are multiples of 3 or 5, we get 3, 5, 6 and 9. 
The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
*/


public class p1_multiple_3and5 {
    public static void main(String[] args){
        
        //Define total variable
        int total = 0;

        // Declare I
        int i;

        //Loop thru 1-999
        for(i = 1; i < 1000; i++ ){

            //Determine whether I is a multiple of 3 and 5 and store them in separarte variables
            boolean multipleOfThree = (i % 3 == 0);
            boolean multipleOfFive = (i % 5 == 0);
            

            //If either statement is true, add I to the total.
            if(multipleOfFive || multipleOfThree)
            {
                total += i;
            }
            
        }

        //Print the total
        System.out.println(total);
    }
}