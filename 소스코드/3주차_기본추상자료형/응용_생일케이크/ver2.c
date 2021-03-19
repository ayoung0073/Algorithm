#include <stdio.h>
#include <stdlib.h>

#define SIZE 100
// 배열로 구현 ver1

typedef struct 
{
    int V[SIZE];
    int n;
}ArrayList;

void init(ArrayList* A) // ArrayList 초기화 
{
    A -> n = 0;
}

void remove_node(ArrayList* A, int pos) // 노드 제거
{
    for (int i = pos; i < A->n - 1; i++) // 역순
        A->V[i] = A->V[i + 1];
    A->n--;
}

void buildList(ArrayList* A, int n)
{
    for(int i = 0; i < n; i++)
        A->V[i] = i + 1;
}

void traverse(ArrayList* A) // 순회 메서드
{
    for(int i = 0; i < A -> n; i++)
        printf("[%d] ", A -> V[i]);
    printf("\n");
}

int runSimulation(ArrayList* A, int n, int k)
{
    int r = 0;
    while (n > 1)
    {
        r = (r + k) % n;
        remove_node(A, r);
        traverse(A);
        n--;
    }
    return A->V[0];
}

int candle(int n, int k) // 배열 사이즈, 간격 
{
    ArrayList A;
    init(&A);
    A.n = n;
    buildList(&A, n);
    int ret = runSimulation(&A, n, k);

    return ret;
}

int main()
{
    printf("%d\n", candle(7, 3));
    return 0;
}
