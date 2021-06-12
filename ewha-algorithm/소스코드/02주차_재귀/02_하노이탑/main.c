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

int main()
{
    rHanoi(4, 'A', 'B', 'C');
    return 0;
}

/*
Disk 1 : Move from A to B
Disk 2 : Move from A to C
Disk 1 : Move from B to C
Disk 3 : Move from A to B
Disk 1 : Move from C to A
Disk 2 : Move from C to B
Disk 1 : Move from A to B
Disk 4 : Move from A to C
Disk 1 : Move from B to C
Disk 2 : Move from B to A
Disk 1 : Move from C to A
Disk 3 : Move from B to C
Disk 1 : Move from A to B
Disk 2 : Move from A to C
Disk 1 : Move from B to C
*/