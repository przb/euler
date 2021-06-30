/*
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
*/

import java.util.ArrayList;

public class p3_prime_factors{   
    
    //This method will check to see if the modulus of the dividend and the divisor is 0. 
    //If it was 0, then the resulting quotent is an integer.
    
    public static void main(String[] args){


        //Make an empty arraylist to store all the factors
        ArrayList<Integer> factors = new ArrayList<Integer>();
        
        //Set a constant equal to the value I am trying to find the factors of.
        final long FINAL_TARGET = 600851475143L;

        //Set the target equal to the final value
        long target = FINAL_TARGET;
        
        //Start with potential factor equal to 3, not 0 or 1 because of math prime numbers and 2 is checked later
        int potentialFactor = 3;

        //Set the max factor to 0, as this will be changed later
        int maxFactor = 0;
        
        //If the target is divisible by two, loop until it isnt.
        while (target % 2 == 0){
            target = target / 2;
            factors.add(2);
        }

        //Once the target is one, all the factors would be found, so the loop can stop looking for factors
        while(target != 1){

            //Checks to see if the potential factor is a factor by seeing the modulus of the big number and the potential factor
            if(target % potentialFactor ==0){

                //Set new target to be the old target, divided by the factor.
                target = target / potentialFactor;

                ///Add the factor to the factors arraylist
                factors.add(potentialFactor);
            }
            else{
                //If it is not a factor, then increment the potential factor
                potentialFactor = potentialFactor + 2;
            }
        }

        //Print all the factors
        System.out.println(factors);


        //Find the max factor in the arraylist
        for (Integer factor : factors) {
            maxFactor = Math.max(maxFactor, factor);
        }

        //Print the max factor
        System.out.println(maxFactor);
        
    }
    

}