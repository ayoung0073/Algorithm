#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define MAX_SIZE 15
#define SWAP(x, y, t) ((t) = (x), (x) = (y), (y) =  (t))
#define LIMIT 5



int partition(int list[], int left, int right, int k)
{
    int pivot, temp, low, high;
    
    pivot = list[k];
    SWAP(list[k], list[right], temp);
    
    printf("Pivot = %d\n", pivot);
    for (int i = 0; i < MAX_SIZE; i++)
        printf("[%d] ", list[i]);
    printf("\n\n");

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

        // for (int i = 0; i < MAX_SIZE; i++)
        //     printf("[%d] ", list[i]);
        // printf("\nlow = %d, high = %d\n", low, high);

        if (low < high) // 교환 대상일 경우
            SWAP(list[low], list[high], temp);
    }while (low < high);

    SWAP(list[low], list[right], temp); // 피벗과 작은 값 교환(여기서는 high <= low)
    printf("피벗의 위치: %d\n", low);

    return low; // 피벗의 위치 반환
}

void quick_sort(int list[], int left, int right)
{
    if (left < right)
    {
        int k = rand() % (right - left) + left + 1;
        int q = partition(list, left, right, k); // 분할을 위한 함수
        quick_sort(list, left, q - 1);
        quick_sort(list, q + 1, right);
    }
}

void rQuickSort(int list[], int left, int right)
{
    if (right - left >= LIMIT)
    {
        int k = rand() % (right - left) + left + 1;
        int m = partition(list, left, right, k); // 분할을 위한 함수
        rQuickSort(list, left, m - 1);
        rQuickSort(list, m + 1, right);
    }
}

void insertionSort(int list[], int n) // 배열과 배열원소 개수
{
    int i, j, save; 
    for (i = 1; i < n; i++)
    {
        save = list[i];
        for(j = i - 1; j >= 0 && list[j] > save; j--) // j 조건 범위 체크하기 !
            list[j + 1] = list[j];
        list[j + 1] = save;
    }
}

void quickSort(int list[])
{
    rQuickSort(list, 0, MAX_SIZE - 1);
    insertionSort(list, MAX_SIZE - 1);
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
[4] [59] [11] [95] [43] [87] [7] [92] [80] [27] [24] [94] [44] [67] [68] 


Pivot = 7
[4] [59] [11] [95] [43] [87] [68] [92] [80] [27] [24] [94] [44] [67] [7] 

Pivot = 43
[4] [7] [11] [95] [59] [87] [68] [92] [80] [27] [24] [94] [44] [67] [43] 

Pivot = 27
[4] [7] [11] [24] [27] [43] [68] [92] [80] [59] [95] [94] [44] [67] [87] 

Pivot = 24
[4] [7] [11] [24] [27] [43] [68] [92] [80] [59] [95] [94] [44] [67] [87] 

Pivot = 92
[4] [7] [11] [24] [27] [43] [68] [87] [80] [59] [95] [94] [44] [67] [92] 

Pivot = 67
[4] [7] [11] [24] [27] [43] [68] [87] [80] [59] [44] [67] [92] [95] [94] 

Pivot = 59
[4] [7] [11] [24] [27] [43] [44] [59] [67] [87] [68] [80] [92] [95] [94] 

Pivot = 80
[4] [7] [11] [24] [27] [43] [44] [59] [67] [87] [68] [80] [92] [95] [94] 

Pivot = 94
[4] [7] [11] [24] [27] [43] [44] [59] [67] [68] [80] [87] [92] [95] [94] 


[4] [7] [11] [24] [27] [43] [44] [59] [67] [68] [80] [87] [92] [94] [95] 
*/