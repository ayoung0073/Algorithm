#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <unistd.h>

#define MAX_SIZE 15
#define SWAP(x, y, t) ((t) = (x), (x) = (y), (y) = (t))

/*
-----------
5 3 8 1 2 7
3 5 8 1 2 7
3 5 1 8 2 7
3 5 1 2 8 7
3 5 1 2 7 8
-----------
한 번의 스캔 : 마지막 숫자 정렬됨
*/
void bubble_sort(int list[], int n)
{
    int temp;
    printf("정렬할 원소 : ");
    for(int t = 0; t < n; t++)
        printf("%d ", list[t]);
    printf("\n\n<<<<<<<<<< 버블 정렬 수행 >>>>>>>>>>");
    for (int i = n - 1; i > 0; i--)
    {
        printf("\n%d 단계>> \n", n - i);
        for (int j = 0; j < i; j++)
            if(list[j] > list[j + 1])
                SWAP(list[j], list[j + 1], temp);

        for (int t = 0; t < n; t++)
            printf("%3d", list[t]);
    }
}

int main()
{

    int list[6] = {5, 3, 8, 1, 2, 7};
    bubble_sort(list, 6);

    return 0;
}

/*
정렬할 원소 : 5 3 8 1 2 7 

<<<<<<<<<< 버블 정렬 수행 >>>>>>>>>>
1 단계>> 
  3  5  1  2  7  8
2 단계>> 
  3  1  2  5  7  8
3 단계>> 
  1  2  3  5  7  8
4 단계>> 
  1  2  3  5  7  8
5 단계>> 
  1  2  3  5  7  8
*/