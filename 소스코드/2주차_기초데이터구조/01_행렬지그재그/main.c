#include <stdio.h>
#define SIZE 5

void zigzag(int A[][SIZE])
{
    int value = 1;
    for (int i = 0; i < SIZE; i++)
    {
        if (i % 2 == 0) // 행 짝수인 경우
            for (int j = 0; j < SIZE; j++) // left -> right
                A[i][j] = value++;
        else // 행 홀수인 경우
            for (int j = SIZE - 1; j >= 0; j--)
                A[i][j] = value++;
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
    int A[SIZE][SIZE] = {0};
    zigzag(A);
    printArray(A);

    return 0;
}

/*
 1  2  3  4  5 
10  9  8  7  6 
11 12 13 14 15 
20 19 18 17 16 
21 22 23 24 25 
*/