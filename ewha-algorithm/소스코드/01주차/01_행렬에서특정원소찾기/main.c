#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define ROWS 8
#define COLS 8

void makeArray(int A[][COLS])
{
    for (int r = 0; r < ROWS; r++)
        for (int c = 0; c < COLS; c++)
            A[r][c] = rand() % 100; // rand() : 0~32767 사이의 숫자
}

void printArray(int A[][COLS])
{
    for (int r = 0; r < ROWS; r++)
    {
        for(int c = 0; c < COLS; c++)
            printf("%2d ", A[r][c]);
        printf("\n");
    }
    printf("\n");
}

int findRow(int A[], int key)
{
    for(int c = 0; c < COLS; c++)
        if (A[c] == key)
            return c;
    return -1;
}

void findMatrix(int A[][COLS], int key)
{
    int r = 0; // 0으로 초기화
    int index;
    while (r < ROWS)
    {
        index = findRow(A[r], key);
        if (index >= 0)
        {
            printf("%d행 %d열에서 %d 발견\n", r, index, key);
            return;
        }
        else
            r++;
    }
    printf("Not Found\n");
}

int main()
{
    int A[ROWS][COLS];
    srand(time(NULL)); // 다른 난수 발생 
    makeArray(A);
    printArray(A);

    int key;
    printf("Input a key value : ");
    scanf("%d", &key);
    findMatrix(A, key);
    
    return 0;
}