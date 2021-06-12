#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define ROWS 8
#define COLS 8

void makeArray(int A[][COLS])
{
    for (int r = 0; r < ROWS; r++)
    {
        int count = rand() % 8;
        for (int i = 0; i < count; i++)
            A[r][i] = 1;
        for (int j = count; j < COLS; j++)
            A[r][j] = 0;
    }
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

void mostOnesButSlow(int A[][COLS]) // O(n ^ 2)
{
    int jmax = 0;
    int i, j, row;
    for(i = 0; i < ROWS; i++)
    {
        j = 0;
        while(j < COLS && A[i][j] == 1)
            j++;
        if (j > jmax)
        {
            row = i;
            jmax = j;
        }
    }
    printf("%d행에 %d개의 1이 최대값임\n", row, jmax);
}

int mostOnes(int A[][COLS]) // O(n)
{
    int i = 0, j = 0;
    int row;
    
    while(1)
    {
        while(A[i][j] == 1)
        {
            j++; // i행에서의 마지막 1의 열(j)을 찾음
            if(j == COLS - 1) // 만약 끝까지 1이면 해당 행 반환
             return i;
        }
        
        row = i; // 우리가 찾는 행 row
        while(A[i][j] == 0) // 위에서 아래로(그 다음 행의 해당 열을 봄)
        // 해당 열이 1인 행을 찾는다. 마지막 행까지 갔는데 없으면 row 반환
        // 1인 행을 찾으면 밖의 while문 반복
        {
            i++; // 다음 행
            if(i == COLS - 1)
                return row;
        }
    }
}

int main()
{
    int A[ROWS][COLS];
    srand(time(NULL)); // 다른 난수 발생 
    makeArray(A);
    printArray(A);
    
    //getchar(); // 화면을 잠깐 멈춤
    mostOnesButSlow(A);
    printf("최대 1행은 %d행입니다. \n", mostOnes(A));
    

    return 0;
}