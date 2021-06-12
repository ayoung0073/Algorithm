#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <unistd.h>

#define MAX_SIZE 15
#define SWAP(x, y, t) ((t) = (x), (x) = (y), (y) = (t))

// // 제자리 삽입 정렬 // 비교하기
// void insertion_sort(int list[], int n) // 배열과 배열원소 개수
// {
//     int i, j, save; 
//     for (i = 1; i < n; i++)
//     {
//         save = list[i];
//         for(j = i - 1; j >= 0 && list[j] > save; j--) // j 조건 범위 체크하기 !
//             list[ㅇㅇj + 1] = list[j];
//         list[j + 1] = save;
//     }
// }

void inc_insertion_sort(int list[], int first, int last, int gap) 
{
    int i, j, key; 
    for (i = first + gap; i <= last; i = i + gap)
    {
        key = list[i];
        for(j = i - gap; j >= first && list[j] > key; j = j - gap) // j 조건 범위 체크하기 !
            list[j + gap] = list[j];
        list[j + gap] = key;
    }
}

void shell_sort(int list[], int n)
{
    int i, gap;
    for (gap = n / 2; gap > 0; gap = gap / 2)
    {
        if (gap % 2 == 0) // 갭이 짝수인 경우, 홀수로 바꿔줌(성능 측)
            gap++;
        for(i = 0; i < gap; i++)
            inc_insertion_sort(list, i, n - 1, gap); // (배열, 첫번째 인덱스, 마지막 인덱스, 갭)
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

    shell_sort(list, MAX_SIZE);

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
/*

25 79 2 50 21 54 71 44 97 82 70 59 51 12 58 


2 12 21 25 44 50 51 54 58 59 70 71 79 82 97 

*/