/*
Each new term in the Fibonacci sequence is generated 
by adding the previous two terms. By starting with 
1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci 
sequence whose values do not exceed four million, 
find the sum of the even-valued terms.
*/

import java.util.*;

public class p2_fibonacci_sum {
    public static void main(String[] args){

        //Make an arraylist with the first two elements of the fibonacci sequence
        ArrayList<Integer> Fibonacci=new ArrayList<Integer>();
        Fibonacci.add(1);
        Fibonacci.add(2);

        //Initialize some variables
        int lastValue;
        int secondLastValue;
        int newValue;
        int len;

        //Loop forever
        while(true){

            //Set the len equal to one less than the number of elements 
            len = Fibonacci.size() - 1;

            //Set the last value equal to the last element
            lastValue = Fibonacci.get(len);

            //Set the secondLastValue equal to the second to last element
            secondLastValue = Fibonacci.get(len - 1);

            //Set the new value equal to the sum of the last value and the second to last value
            newValue = lastValue + secondLastValue;           
            
            //If the new value is more than 4,000,000, then stop
            if (newValue > 4000000){
                break;
            }

            //Otherwise, continue
            else{
                Fibonacci.add(newValue);
            }
        }


        //I really dont know what ihis part does exactly, other than it converts the ArrayList to an Array found it online
        Integer finalArray[] = new Integer[Fibonacci.size()];
        finalArray = Fibonacci.toArray(finalArray);

        //Define and assign the total varliable.
        int total = 0;

        //loop throught all the even numbers and add them to the total
        for (int i : finalArray) {
            boolean even = (i % 2 == 0);
            if(even){
                total += i;
            }
        }

        //Print the results
        System.out.println(total);
    }   
}
