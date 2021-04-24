#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <unistd.h>

#define MAX_SIZE 15
#define SWAP(x, y, t) ((t) = (x), (x) = (y), (y) = (t))

void selection_sort(int list[], int n) // n개의 배열 원소
{
    int least, temp;
    
    for (int i = 0; i < n - 1; i++)
    {
        least = i; // 인덱스로
        for (int j = i + 1; j < n; j++)
        {
            if (list[least] > list[j])
                least = j;
        }
        SWAP(list[i], list[least], temp);
    }
}

int main()
{
    int list[MAX_SIZE];
    srand(time(NULL)); // seed값 넣어주기

    for (int i = 0; i < MAX_SIZE; i++)
    {
        list[i] = rand() % 100;
        for(int j = 0; j < i; j++) // 중복 제거
            if(list[i] == list[j])
                i--;
    }

    for (int i = 0; i < MAX_SIZE; i++)
        printf("%d ", list[i]);
    printf("\n\n"); getchar();

    selection_sort(list, MAX_SIZE);

    for(int i = 0; i< MAX_SIZE; i++)
    {
        printf("%d ", list[i]);
        // sleep(1); // 출력 후 잠시 멈추기 // Windows.h
        fflush(stdout);    // 리눅스에서는 문자 하나씩 출력한 뒤 usleep으로 기다리려면
                           // 출력 버퍼를 비워야 함
        usleep(500000);    // 리눅스에서 0.5초를 기다릴 때(-std=gnu99 옵션 사용)
    }

    printf("\n\n");
}