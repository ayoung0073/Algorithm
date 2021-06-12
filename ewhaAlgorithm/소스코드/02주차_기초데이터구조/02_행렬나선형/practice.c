#include <stdio.h>
#define SIZE 100

void sprial(int A[][SIZE], int r, int c)
{
    int top = 0, bottom = r - 1, left = 0, right = c - 1;

    int value = 1;
    int i = 0, j = 0;

    while (top <= bottom && left <= right)
    {
        // 왼쪽 -> 오른쪽 이동
        for (j = left; j <= right; j++)
        {
            A[top][j] = value++;
        }
        top++;

        if (top <= bottom)
        {
            for (i = top; i <= bottom; i++)
            {
                A[i][right] = value++;
            }
            right--;
        }

        if (left <= right)
        {
            for (j = right; j >= left; j--)
            {
                A[bottom][j] = value++;
            }
            bottom--;
        }

        if (top <= bottom)
        {
            for(i = bottom; i >= top; i--)
            {
                A[i][left] = value++;
            }
            left++;
        }
    }
}

void printArray(int A[][SIZE], int r, int c)
{
    for (int i = 0; i < r; i++)
    {
        for (int j = 0; j < c ;j++)
            printf("%2d ", A[i][j]);
        printf("\n");
    }
}

int main()
{
    int A[SIZE][SIZE];
    int r, c;

    scanf("%d %d", &r, &c);
    printf("%d %d\n", r, c);
    sprial(A, r, c);
    printArray(A, r, c);
    return 0;
}