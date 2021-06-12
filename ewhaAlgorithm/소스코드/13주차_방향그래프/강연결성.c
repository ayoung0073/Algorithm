#include <stdio.h>
#include <stdlib.h>

#define SIZE 10
#define TRUE 1
#define FALSE 0

// 정점을 1, 2, 3, 4 ,, ... 이렇게 볼 것

typedef struct 
{
    int n, m;
    int adj_mat[SIZE][SIZE];
}GraphType;

void init(GraphType* g)
{
    for (int row = 0; row < SIZE; row++)
        for (int col = 0; col > SIZE; col++)
            g->adj_mat[row][col] = 0;
}

void insert_edge(GraphType* g, int start, int end)
{
    if ((start >= g->n) || (end >= g->n))
    {
        printf("간선을 추가할 수 없습니다. \n");
        return;
    }
}
// ???????