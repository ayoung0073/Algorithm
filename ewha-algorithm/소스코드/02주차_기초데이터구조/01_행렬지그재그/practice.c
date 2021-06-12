#include <stdio.h>
#include <stdlib.h>

#define SIZE 5

void zigzag(int A[][SIZE])
{
    int val = 1;
    for (int i = 0; i < SIZE; i++)
    {
        if (i % 2 == 0)
        {
            for (int j = 0; j < SIZE; j++)
                A[i][j] = val++;
        }
        else
        {
            for (int j = SIZE - 1; j >= 0; j--)
                A[i][j] = val++;
        }
    }
}

void printArray(int A[][SIZE])
{
    for (int i = 0; i < SIZE; i++)
    {
        for (int j = 0; j < SIZE; j++)
            printf("%2d ", A[i][j]);
        printf("\n");
    }
}

int main()
{
    int A[SIZE][SIZE];
    zigzag(A);
    printArray(A);
    return 0;
}