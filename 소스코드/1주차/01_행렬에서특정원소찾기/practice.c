#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define ROWS 8
#define COLS 8

/*
makeArray(int A[][COLS])
printArray(int A[][COLS])
findMatrix(int A[][COLS], int key)
findRow(int A[], int key)
*/

void makeArray(int A[][COLS])
{
    for (int i = 0; i < ROWS; i++)
        for (int j = 0; j < COLS; j++)
            A[i][j] = rand() % 100;
}

void printArray(int A[][COLS])
{
    for (int i = 0; i < ROWS; i++)
    { // 중괄호 꼭 붙이기
        for (int j = 0; j < COLS; j++)
            printf("[%d] ", A[i][j]);
        printf("\n");
    }
}

int findRow(int A[], int key)
{
    for (int i = 0; i < COLS; i++)
    {
        if (A[i] == key)
        {
            return i;
        }
    }
    return -1;
}

void findMatrix(int A[][COLS], int key)
{
    int index;
    for (int i = 0; i < ROWS; i++)
    {
        index = findRow(A[i], key);
        if (index >= 0)
        {
            printf("%d행 %d열에서 %d 발견\n", i, index, key);
            return;
        }
    }
    printf("해당 키를 찾지 못함\n");
}

int main()
{
    int A[ROWS][COLS];
    srand(time(NULL));
    makeArray(A);
    printArray(A);

    int key;

    printf("찾고 싶은 key 입력 : ");
    scanf("%d", &key);
    findMatrix(A, key);
    return 0;
}