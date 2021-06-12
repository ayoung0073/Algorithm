#include <stdio.h>
#include <stdlib.h>

#define N 100

void printArr(int arr[], int n)
{
    for (int i = 0; i < n; i++)
        printf("[%d] ", arr[i]);
    printf("\n");
}

void subset(int arr[], int setSize, int n, int idx) // 부분집합 구하기
{
    if (idx == n)
    {
        printArr(arr, setSize);
        return;
    }
    arr[setSize] = idx;

    subset(arr, setSize + 1, n, idx + 1); // 집합 사이즈 추가
    subset(arr, setSize, n, idx + 1); // 집합 사이즈는 그대로
}

int main()
{
    int arr[N], n;
    scanf("%d", &n); // 집합 원소의 개수
    subset(arr, 0, n, 0);
}


/* 
3
[0] [1] [2] 
[0] [1] 
[0] [2] 
[0] 
[1] [2] 
[1] 
[2] 

5
[0] [1] [2] [3] [4] 
[0] [1] [2] [3] 
[0] [1] [2] [4] 
[0] [1] [2] 
[0] [1] [3] [4] 
[0] [1] [3] 
[0] [1] [4] 
[0] [1] 
[0] [2] [3] [4] 
[0] [2] [3] 
[0] [2] [4] 
[0] [2] 
[0] [3] [4] 
[0] [3] 
[0] [4] 
[0] 
[1] [2] [3] [4] 
[1] [2] [3] 
[1] [2] [4] 
[1] [2] 
[1] [3] [4] 
[1] [3] 
[1] [4] 
[1] 
[2] [3] [4] 
[2] [3] 
[2] [4] 
[2] 
[3] [4] 
[3] 
[4] 
*/