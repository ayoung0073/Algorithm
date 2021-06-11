#include <stdlib.h>
#include <stdio.h>

#define min(x, y) ((x) > (y) ? (y) : (x))

int A[] = {0, 1, 3, 6, 11, 17};
int H[] = {0, 2, 5, 1, 5, 0};

int m[10];

int airtel(int n)
{
    m[0] = 0; 
    int cost;
    for (int d = 1; d <= n; d++) // 등호들어가야한다.
    {
        m[d] = 10000; // 무한대라고 정의
        for (int k = 0; k < d; k++)
        {
            cost = m[k] + H[k] + A[d-k];
            m[d] = min(m[d], cost);
        }
    }
    return m[n];
}

int rAirtelForward(int d) // 분할 통치법 정방향
// d : 도착도시 d
{
    if (d == 0)
        return 0;
    int minCost = 10000;
    int cost;

    for (int k = 0; k < d; k++) // k : 도시
    {
        cost = rAirtelForward(k) + H[k] + A[d - k];
        minCost = min(minCost, cost);
    }
    return minCost;
}

int main()
{
    printf("%d\n", rAirtelForward(5));
    printf("%d\n", airtel(5));
    // 10
    return 0;
}