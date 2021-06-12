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

void buildList(ArrayList* A, int n)
{
    for(int i = 0; i < n; i++)
        A->V[i] = i + 1; // 양초 위치 저장
}

int runSimulation(ArrayList* A, int n, int k)
{
    int r = 0;
    int i;
    int size = n;
    while (n > 1) // 양초가 남아있는 동안 // n이 1인 경우 리턴할 값 생김
    {
        i = 0;
        while(i < k) // 간격만큼 이동
        {
            r = (r + 1) % size; // 원형큐 연산처럼 연산
            if (A->V[r] != 0) // 이미 끈 양초인 경우는 skip(카운트에서 제외)
                i += 1;
        }
        A->V[r] = 0; // 양초 끈다.
        n -= 1; // 남은 양초 횟수 갱신
        while (A->V[r] == 0) // 다음 끌 때 0 아닌 곳을 찾기 위함
            r = (r + 1) % size;
    }
    return A->V[r]; // 배열값에 위치가 저장되어있음
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
