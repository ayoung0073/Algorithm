#include <stdlib.h>
#include <stdio.h>

#define min(x, y) ((x) > (y) ? (y) : (x))

int A[] = {0, 1, 3, 6, 11, 17};
int H[] = {0, 2, 5, 1, 5, 0};

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

// 역방향도 해보쟘. 

int main()
{
    printf("%d\n", rAirtelForward(5));
    // 10
    return 0;
}