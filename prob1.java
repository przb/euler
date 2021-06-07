public class prob1 {
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