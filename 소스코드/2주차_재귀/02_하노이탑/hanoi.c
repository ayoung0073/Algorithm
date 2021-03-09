#include <stdio.h>
#include <stdlib.h>

void rHanoi(int n, char from, char aux, char to) // 이동해야 할 원반 수, 출발, 보조, 목표
{
    if(n == 1)
        printf("Disk %d : Move from %c to %c\n", n, from, to); // 원판 번호
    else
    {
        rHanoi(n - 1, from, to, aux);
        printf("Disk %d : Move from %c to %c\n", n, from, to);
        rHanoi(n - 1, aux, from, to);
    }
}

void main()
{
    rHanoi(4, 'A', 'B', 'C');
}