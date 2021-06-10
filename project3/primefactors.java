/*

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?

*/
package project3;

public class primefactors{
    public static void main(String[] args){
        long TARGET = 600851475143L;
        float factor;

        for(int i = 1; i < TARGET; i ++){
            factor = TARGET / i;
            
            System.out.println(factor);
            //if (){}
        }
    }
}