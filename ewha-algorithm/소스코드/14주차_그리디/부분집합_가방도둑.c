#include <stdio.h>
#include <stdlib.h>

#define N 100

int weight[N], value[N], cap;
int maxSet[N], maxSetSize = 0, maxValue = 0;

void eval_knapsack(int arr[], int setSize)
{
    int currWeight = 0, currValue = 0;

    for (int i = 0; i < setSize; i++)
    {
        currWeight += weight[arr[i]];
        currValue += value[arr[i]];
    }

    if (currWeight > cap) // 현재 무게가 제한 용량보다 큰 경우 종료
        return;

    if (currValue > maxValue) // 현재 무게가 지금까지의 최대 무게보다 큰 경우 gang신
    {
        maxValue = currValue;
        maxSetSize = setSize; 

        for (int i = 0; i < setSize; i++)
            maxSet[i] = arr[i];
    }
}

void subset_knapsack(int arr[], int setSize, int n, int idx) // 부분집합 구하기
{
    if (idx == n)
    {
        // 최댓값 계산 함수
        eval_knapsack(arr, setSize);
        return;
    }
    arr[setSize] = idx;

    subset_knapsack(arr, setSize + 1, n, idx + 1);
    subset_knapsack(arr, setSize, n, idx + 1);
}

void printArr(int arr[], int n)
{
    for (int i = 0; i < n; i++)
        printf("[%d] ", arr[i]);
    printf("\n");
}


int main()
{
    int arr[N], n;
    scanf("%d %d", &n, &cap); // 물건의 개수와 가방의 용량

    for (int i = 0; i < n; i++)
        scanf("%d", &value[i]);
    for (int i = 0; i < n; i++)
        scanf("%d", &weight[i]);

    subset_knapsack(arr, 0, n, 0);

    printf("Max value : %d\n", maxValue);
    printArr(maxSet, maxSetSize);
}

/*
10 20
2 3 3 4 4 5 7 8 8 9
3 5 7 4 3 9 2 9 5 10
Max value : 28
[4] [6] [8] [9]
*/