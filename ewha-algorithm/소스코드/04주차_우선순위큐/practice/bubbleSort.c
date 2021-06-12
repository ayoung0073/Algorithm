#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <unistd.h>

#define MAX_SIZE 15
#define SWAP(x, y, t) ((t) = (x), (x) = (y), (y) = (t))

void bubble_sort(int list[], int n)
{
    int temp;
    // 마지막 숫자는 정렬된다.
    for (int i = n - 1; i >= 0; i--)
    {
        for (int j = 0; j < i; j++)
        {
            if (list[j] > list[j + 1])
                SWAP(list[j], list[j + 1], temp);
        }
    }
}

int main()
{

    int list[6] = {5, 3, 8, 1, 2, 7};
    bubble_sort(list, 6);

    for(int i = 0; i< 6; i++)
    {
        printf("%d ", list[i]);
        // sleep(1); // 출력 후 잠시 멈추기 // Windows.h
        fflush(stdout);    // 리눅스에서는 문자 하나씩 출력한 뒤 usleep으로 기다리려면
                           // 출력 버퍼를 비워야 함
        usleep(500000);    // 리눅스에서 0.5초를 기다릴 때(-std=gnu99 옵션 사용)
    }

    return 0;
}