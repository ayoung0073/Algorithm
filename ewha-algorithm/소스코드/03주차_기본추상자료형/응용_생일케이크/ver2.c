#include <stdio.h>
#include <stdlib.h>

#define SIZE 100
// 배열로 구현 ver2 // 아예 뽑아내는 경우

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

int runSimulation(ArrayList* A, int n, int k)
{
    int r = 0;
    while (n > 1)
    {
        r = (r + k) % n; // 원형큐 연산처럼 연산(remove할 인덱스)
        remove_node(A, r);
        n--;
    }
    return A->V[0]; // n = 1인 경우이므로, 하나만 남아있음.
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
    printf("%d\n", candle(13, 3));
    printf("%d\n", candle(22, 5));
    return 0;
}
