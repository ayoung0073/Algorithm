#include <stdio.h>
#include <stdlib.h>

#define MAX_SIZE 5
#define SWAP(x, y, t) ((t) = (x), (x) = (y), (y) =  (t))

typedef struct ArrayList
{
    int list[MAX_SIZE];
    int n;
}ArrayList;

int partition(int list[], int left, int right, int val)
{
    int pivot, temp, low, high, k;
    
    for (int i = left; i <= right; i++)
    {
        if (list[i] == val)
        {
            k = i;
        }
    }

    pivot = val;
    SWAP(list[k], list[right], temp);
    
    
    printf("Pivot = %d, left = %d, right = %d, k = %d\n", pivot, left, right, k);
    // for (int i = 0; i < MAX_SIZE; i++)
    //     printf("[%d] ", list[i]);
    // printf("\n\n");

    low = left - 1; // index
    high = right; 
    
    do
    {
        do
            low++;
        while(list[low] < pivot);

        do 
            high--;
        while(list[high] > pivot);

        for (int i = 0; i < MAX_SIZE; i++)
            printf("[%d] ", list[i]);
        printf("\nlow = %d, high = %d\n", low, high);

        if (low < high) // 교환 대상일 경우
            SWAP(list[low], list[high], temp);
    }while (low < high);
    
    SWAP(list[low], list[right], temp); // 피벗과 작은 값 교환(여기서는 high <= low)
    printf("피벗의 위치: %d\n결과\n", low);
    for (int i = 0; i < MAX_SIZE; i++)
        printf("[%d] ", list[i]);
    printf("\n\n");
    return low; // 피벗의 위치 반환
}

void match(int B[], int R[], int left, int right)
{
    if (left > right) {};

    int b = rand() % (right - left) + left - 1;
    printf("\n\n===========링 정렬 시작\n\n");
    int e = partition(R, left, right, B[b]); // Ring을 나눔 // 같은 크기를 가진 인덱스 반환
    printf("신부%d[%d]와 크기가 같은 ring 인덱스: %d[%d]\n", b, B[b], e, R[e]);
    for (int i = 0; i < MAX_SIZE; i++)
        printf("[%d] ", R[i]);
    printf("\n\n===========\n신부 정렬 시작\n\n");
    int q = partition(B, left, right, R[e]); // 신부를 정렬하자
    printf("\n\n===========\n\n");
    printf("%d를 기준으로 신부 정렬\n", R[e]);
    for (int i = 0; i < MAX_SIZE; i++)
        printf("[%d] ", B[i]);
    printf("\n\n===========\n\n");
    match(B, R, left, q - 1);
    match(B, R, q + 1, right);

}

int main()
{
    int list[MAX_SIZE];
    int B[MAX_SIZE] = {15, 13, 12, 20, 22};
    int R[MAX_SIZE] = {13, 22, 15, 12, 20};

    match(B, R, 0, MAX_SIZE - 1);
    printf("\n");
    printf("신부 정렬\n");
    for (int i = 0; i < MAX_SIZE; i++)
        printf("[%d] ", B[i]);

    printf("\n\n반지 정렬\n");
    for (int i = 0; i < MAX_SIZE; i++)
        printf("[%d] ", R[i]);
    printf("\n\n");
}
