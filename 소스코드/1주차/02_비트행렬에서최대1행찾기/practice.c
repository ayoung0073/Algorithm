#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define ROWS 8
#define COLS 8

/*
makeArray(int A[][COLS]);
printArray(int A[][COLS]);
mostOnesButSlow(int A[][COLS]); // 느린 알고리즘
mostOnes(int A[][COLS]);
*/

void makeArray(int A[][COLS])
{
    int i;
    for (int r = 0; r < ROWS; r++)
    {
        int count = rand() % 8;
        for (i = 0; i < count; i++)
            A[r][i] = 1;
        for (i = count; i < COLS; i++)
            A[r][i] = 0;
    }
}

void printArray(int A[][COLS])
{
    for (int r = 0; r < ROWS; r++)
    {
        for (int c = 0; c < COLS; c++)
            printf("%d ", A[r][c]);
        printf("\n");
    }
}

int mostOnesButSlow(int A[][COLS])
{
    int max_row = 0;
    int max_cnt = 0;
    int cnt;
    // 각 행마다 1의 개수 찾기
    for (int r = 0; r < ROWS; r++)
    {
        cnt = 0;
        for (int c = 0; c < COLS; c++)
        {
            if (A[r][c] == 1)
                cnt++;
            else break;
        }
        if (max_cnt < cnt) 
        {
            max_cnt = cnt;
            max_row = r;
        }
    }
    return max_row;
}

int mostOnes(int A[][COLS])
{
    // 기억해야 할 col 변수 있어야 함
    int i = 0, j = 0;
    int row;

    while (1)
    {
        while (A[i][j] == 1)
        {
            j++;
            if (j == COLS  - 1)  // 모든 열이 1인 경우(최대 행)
                return i;
        }

        row = i;
        i++;

        // 이제 위에서 아래로
        while (A[i][j] == 0) // A[i][j]가 1인 행 찾기
        {
            i++;
            if (i == ROWS - 1)
                return row;
        }
    }
    
}

int main()
{
    int A[ROWS][COLS];
    srand(time(NULL));
    makeArray(A);
    printArray(A);

    // int max_row = mostOnesButSlow(A);
    int max_row = mostOnes(A);
    printf("1의 개수가 최대인 행은 %d 행입니다. \n", max_row);
}