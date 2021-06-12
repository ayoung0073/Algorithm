#include <stdio.h>
#include <stdlib.h>

int c[15][150];

void calculate_subset_sum(int s[], int n, int m)
{
    int i, j;

    for (i = 0; i <= n; i++)
        c[i][0] = 1;

    for (i = 1; i <= m; i++)
        c[0][i] = 0;

    for (i = 1; i <= n; i++) // 행
    {
        for (j = 1; j <= m; j++) // 열
        {
            c[i][j] = 0; // 초기화 

            if (j >= s[i - 1])
                if (c[i - 1][j - s[i - 1]] == 1)
                    c[i][j] = 1;
            if (c[i - 1][j] == 1)
                c[i][j] = 1;
        }
    }

}

int main()
{
    int m, n;
    printf("input m, n : ");
    scanf("%d %d", &m, &n);
    int* s = (int*)malloc(sizeof(int));

    for (int i = 0; i < n; i++)
        scanf("%d", &s[i]);

    calculate_subset_sum(s, n, m);
    
    if (c[n][m] == 1) 
    {
        printf("Possible\n");
        for (int i = 1; i < m; i++)
        {
            if (c[n][i] == 1)
                printf("%d ", i);
        }
    }
}

// 부분집합의 합이 7이 될 수 있나
/*
input m, n : 7 3 
2 5 8
Possible
2 5 
*/