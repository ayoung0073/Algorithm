#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <unistd.h>

#define MAX_SIZE 15
#define SWAP(x, y, t) ((t) = (x), (x) = (y), (y) = (t))

void insertion_sort(int list[], int n)
{
    int i, j, save;

    for (i = 1; i < n; i++)
    {
        save = list[i];
        for (j = i - 1; j >= 0 && list[j] > save; j--)
        {
            list[j + 1] = list[j];
        }
        list[j + 1] = save;
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

    insertion_sort(list, MAX_SIZE);

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