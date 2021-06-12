#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define SIZE 8

// 누적평균 (1차원 배열)

void makeArray(int A[])
{
    for(int i = 0; i < SIZE; i++)
        A[i] = rand() % 50 + 50; // 50~99까지의 숫자
}

void printArray(int A[])
{
    for (int i = 0; i < SIZE; i++)
        printf("[%d] ", A[i]);
    printf("\n");
}

void prefixAVG1(int A[]) // O(n^2)
{
    int X[SIZE];
    int sum;
    for (int i = 0; i < SIZE; i++)
    {
        sum = 0;
        for (int j = 0; j <= i; j++)
            sum += A[j];
        X[i] = sum / (i + 1);
    }
    printArray(X);
}

void prefixAVG2(int A[]) // O(n)
{
    int X[SIZE];
    int sum = 0;
    for (int i = 0; i < SIZE; i++)
    {
        sum += A[i];
        X[i] = sum / (i + 1);
    }
    printArray(X);
}

int main()
{
    int A[SIZE];
    srand(time(NULL));
    makeArray(A);
    printArray(A);
    getchar();
    
    prefixAVG1(A);
    prefixAVG2(A);
}