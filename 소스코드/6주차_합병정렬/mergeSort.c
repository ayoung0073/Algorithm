#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <unistd.h>

#define MAX_SIZE 15
int sorted[MAX_SIZE]; // 입력 배열을 대상으로 합병 정렬을 했을 때 정렬된 배열 저장

void merge(int list[], int left, int mid, int right)
{
    int i = left;
    int j = mid + 1;
    int k = left;
    int l; // 반복문 돌릴 변수 선언

    while (i <= mid && j <= right)
    {
        if (list[i] <= list[j]) sorted[k++] = list[i++];
        else sorted[k++] = list[j++];
    }

    if (i > mid)
        for (l = j; l <= right; l++) sorted[k++] = list[l];
    else
        for (l = i; l <= mid; l++) sorted[k++] = list[l];

    for (l = left; l <= right; l++)
        list[l] = sorted[l];
}

void merge_sort(int list[], int left, int right)
{
    int mid;
    if (left < right) // 분할 가능 조건
    {
        mid = (left + right) / 2;
        merge_sort(list, left, mid);
        merge_sort(list, mid + 1, right);
        merge(list, left, mid, right);
    }
}

int main()
{
    int list[MAX_SIZE];
    srand(time(NULL));
    for (int i = 0; i < MAX_SIZE; i++)
    {
        list[i] = rand() % 100;
        for (int j = 0; j < i; j++)
            if (list[i] == list[j]) i--;
    }

    for (int i = 0; i < MAX_SIZE; i++)
        printf("[%d] ", list[i]);
    printf("\n\n"); getchar();

    merge_sort(list, 0, MAX_SIZE - 1);

    for (int i = 0; i < MAX_SIZE; i++)
    {
        printf("[%d] ", list[i]);
        fflush(stdout);
        usleep(500000);
    }
    printf("\n");

    return 0;
}
