#include <stdlib.h>
#include <stdio.h>

/**
The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:
13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1

It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), 
it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
*/

/**
 * @brief 
 * 
 * @param n the number to have the algorithm fix
 * @return int the next number in the series. 
 */
int nextCollatz(int n)
{
    if (n % 2 == 0)
    {
        return n / 2;
    }
    else
    {
        return (3 * n) + 1;
    }
}

/**
 * @brief 
 * 
 * @param n first number in the collatz sequence
 * @return int length of the chian with the input N. Count starts at 1.
 */
int collatzChainLength(int n)
{
    int count = 1;

    while (n != 1 && n > 0)
    {
        n = nextCollatz(n);
        count++;
    }

    return count;
}

/**
 * @brief Not neccesary for this problem, but i misread the problem and made so i figured i may as well keep this method
 * 
 * @param n the minimum acceptable chain length
 * @return int the first number that produced the chain with an appropritate length
 */
int findChainLengthOver(int n)
{
    int longestChainSeed = 1;

    while (collatzChainLength(longestChainSeed) < n)
    {
        longestChainSeed++;
    }
    return longestChainSeed;
}

/**
 * @brief 
 * 
 * @param n longest chain under number, n 
 * @return the seed of the number that produced the chain.
 */
int longestChain(int n)
{
    int longestSeed = 1;
    int longestLength = 1;
    for (int i = 1; i < n; i++)
    {
        
        if (longestLength < collatzChainLength(i))
        {
            longestSeed = i;
            longestLength = collatzChainLength(i);
        }
    }
    return longestSeed;
}

int main()
{
    int longestChainSeed = longestChain(1000000);
    int longestChainLength = collatzChainLength(longestChainSeed);
    printf("Longest Chain: %d\nChain Lenght: %d\n", longestChainSeed, longestChainLength);
    return 0;
}