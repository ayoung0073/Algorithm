#include <stdio.h>
#define SIZE 100

void spiral(int A[][SIZE], int n, int m)
{
    int left = 0, right = m - 1;
    int top = 0, bottom = n - 1;
    
    int value = 1;
    
    int i = 0, j = 0;
    
    while (left <= right && top <= bottom)
    {
        for (j = left; j <= right; j++)
            A[top][j] = value++;
        top++;
        
        if (top <= bottom) // 위 -> 아래로 움직이는 경우 조건 체크
        {
            for(i = top; i <= bottom; i++)
                A[i][right] = value++;
            right--;
        }
        
        if (left <= right) // 오른쪽 -> 왼쪽으로 움직이는 경우 조건 체크
        {
            for(j = right; j >= left; j--)
                A[bottom][j] = value++;
            bottom--;
        }
        
        if(top <= bottom) // 아래 -> 위로 움직이는 경우 조건 체크
        {
            for (i = bottom; i >= top; i--)
                A[i][left] = value++;
            left++;
        }
    }

}

void printArray(int A[][SIZE], int n, int m)
{
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < m; j++)
            printf("%2d ", A[i][j]);
        printf("\n");
    }
}

int main()
{
    int A[SIZE][SIZE] = {0};
    int n, m;
    scanf("%d %d", &n, &m);
    spiral(A, n, m);
    printArray(A, n, m);

    return 0;
}

/*
5
4 5                                                                                                                                                                                
 1  2  3  4  5                                                                                                                                                                     
14 15 16 17  6                                                                                                                                                                     
13 20 19 18  7                                                                                                                                                                     
12 11 10  9  8   
*/