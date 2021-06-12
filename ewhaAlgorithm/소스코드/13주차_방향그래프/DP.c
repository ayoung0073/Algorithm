#include <stdio.h>
#include <stdlib.h>

#define M 100
#define N 100

int map[M][N];
int path[M][N];

int num_path(int m, int n) // NO DP
{
    if (map[m][n] == 0)
        return 0;
    if (m == 0 & n == 0)
        return 1;
    return ((m > 0) ? num_path(m - 1, n) : 0) + ((n > 0) ? num_path(m, n - 1) : 0);
}

int calc_path(int m, int n) // 재귀 아님
{
    int i, j;
    path[0][0] = map[0][0];

    for (i = 1; i < m; i++)
        if (map[i][0] == 0)
            path[i][0] = 0;
        else
            path[i][0] = path[i - 1][0];

    for (j = 1; j < n; j++)
        if (map[0][j] == 0)
            path[0][j] = 0;
        else
            path[0][j] = path[0][j - 1];

    for (i = 1; i < m; i++)
        for (j = 1; j < n; j++)
            if (map[i][j] == 0)
                path[i][j] = 0;
            else
                path[i][j] = path[i - 1][j] + path[i][j - 1];

    return path[m - 1][n - 1];
}

void print(int m, int n)
{
    for (int i = 0; i < m; i++)
    {
        for (int j = 0; j < n; j++)
            printf("%d ", path[i][j]);
        printf("\n");
    }
}

int main()
{
    int m, n;
    scanf("%d %d", &m, &n);
    for (int i = 0; i < m; i++)
        for (int j = 0; j < n; j++)
            scanf("%d", &map[i][j]);

    // printf("%d", num_path(m - 1, n - 1));
    printf("%d\n", calc_path(m, n));
    print(m, n);
    return 0;
}

/*
5 5
1 1 1 1 1
1 1 0 0 1
1 1 1 1 1
1 1 1 0 1
0 0 1 1 1
11
1 1 1 1 1 
1 2 0 0 1 
1 3 3 3 4 
1 4 7 0 4 
0 0 7 7 11 
*/