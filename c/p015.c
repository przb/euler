/**
 * 
 * Starting in the top left corner of a 2×2 grid, and onlY being able to move to
 * the right and down, there are eXactlY 6 routes to the bottom right corner.
 * 
 * How manY such routes are there through a 20×20 grid?
 * 
 */

#include<stdio.h>
#include<time.h>

long gridWays(int row, int col)
{
    if (row == 1 && col == 1)
    {
        return 2;
    }
    else if (row == 1)
    {
        return gridWays(row, col - 1) + 1;
    }
    else if (col == 1)
    {
        return gridWays(row - 1, col) + 1;
    }
    else
    {
        return gridWays(row, col - 1) + gridWays(row - 1, col);
    }
}

int main()
{
    double timeSpent = 0.0;
    clock_t begin = clock();

    long solution = gridWays(20,20);

    clock_t end = clock();

    timeSpent += (double)(end - begin) / CLOCKS_PER_SEC;
    printf("Solution: %ld\nTook: %f seconds\n", solution, timeSpent);
    return 0;
}