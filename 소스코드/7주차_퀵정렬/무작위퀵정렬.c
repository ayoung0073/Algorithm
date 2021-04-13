#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define MAX_SIZE 15
#define SWAP(x, y, t) ((t) = (x), (x) = (y), (y) =  (t))

int partition(int list[], int left, int right)
{
    int pivot, temp, low, high;
    
    low = left; // index
    high = right + 1; 
    pivot = list[left];
    
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

    SWAP(list[left], list[high], temp); // 피벗과 작은 값 교환(여기서는 high <= low)
    return high; // 피벗의 위치 반환
}

void quick_sort(int list[], int left, int right)
{
    if (left < right)
    {
        int q = partition(list, left, right); // 분할을 위한 함수
        quick_sort(list, left, q - 1);
        quick_sort(list, q + 1, right);
    }
}

int main()
{
    int list[MAX_SIZE];
    srand(time(NULL));
    for (int i = 0; i < MAX_SIZE; i++)
        list[i] = rand() % 100;
    for (int i = 0; i < MAX_SIZE; i++)
        printf("[%d] ", list[i]);
    printf("\n\n");
    getchar();

    quick_sort(list, 0, MAX_SIZE - 1);
    printf("\n");
    for (int i = 0; i < MAX_SIZE; i++)
        printf("[%d] ", list[i]);
    printf("\n\n");
}

/*
[65] [80] [79] [61] [91] [33] [58] [55] [25] [56] [50] [30] [22] [2] [43] 


[65] [80] [79] [61] [91] [33] [58] [55] [25] [56] [50] [30] [22] [2] [43] 
low = 1, high = 14
[65] [43] [79] [61] [91] [33] [58] [55] [25] [56] [50] [30] [22] [2] [80] 
low = 2, high = 13
[65] [43] [2] [61] [91] [33] [58] [55] [25] [56] [50] [30] [22] [79] [80] 
low = 4, high = 12
[65] [43] [2] [61] [22] [33] [58] [55] [25] [56] [50] [30] [91] [79] [80] 
low = 12, high = 11
[30] [43] [2] [61] [22] [33] [58] [55] [25] [56] [50] [65] [91] [79] [80] 
low = 1, high = 8
[30] [25] [2] [61] [22] [33] [58] [55] [43] [56] [50] [65] [91] [79] [80] 
low = 3, high = 4
[30] [25] [2] [22] [61] [33] [58] [55] [43] [56] [50] [65] [91] [79] [80] 
low = 4, high = 3
[22] [25] [2] [30] [61] [33] [58] [55] [43] [56] [50] [65] [91] [79] [80] 
low = 1, high = 2
[22] [2] [25] [30] [61] [33] [58] [55] [43] [56] [50] [65] [91] [79] [80] 
low = 2, high = 1
[2] [22] [25] [30] [61] [33] [58] [55] [43] [56] [50] [65] [91] [79] [80] 
low = 11, high = 10
[2] [22] [25] [30] [50] [33] [58] [55] [43] [56] [61] [65] [91] [79] [80] 
low = 6, high = 8
[2] [22] [25] [30] [50] [33] [43] [55] [58] [56] [61] [65] [91] [79] [80] 
low = 7, high = 6
[2] [22] [25] [30] [43] [33] [50] [55] [58] [56] [61] [65] [91] [79] [80] 
low = 6, high = 5
[2] [22] [25] [30] [33] [43] [50] [55] [58] [56] [61] [65] [91] [79] [80] 
low = 8, high = 7
[2] [22] [25] [30] [33] [43] [50] [55] [58] [56] [61] [65] [91] [79] [80] 
low = 10, high = 9
[2] [22] [25] [30] [33] [43] [50] [55] [56] [58] [61] [65] [91] [79] [80] 
low = 15, high = 14
[2] [22] [25] [30] [33] [43] [50] [55] [56] [58] [61] [65] [80] [79] [91] 
low = 14, high = 13

[2] [22] [25] [30] [33] [43] [50] [55] [56] [58] [61] [65] [79] [80] [91] 
*/