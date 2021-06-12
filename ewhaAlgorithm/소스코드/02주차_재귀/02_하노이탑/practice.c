#include <stdio.h>

void rHanoi(int n, char from, char aux, char to)
{
    if (n == 1)
        printf("%d개의 원판을 %c에서 %c로 옮긴다.\n", n, from, to);
    else
    {
        rHanoi(n - 1, from, to, aux);
        printf("%d개의 원판을 %c에서 %c로 옮긴다.\n", n, from, to);
        rHanoi(n - 1, aux, from, to);
        // printf("%d개의 원판을 %c에서 %c로 옮긴다.\n", n - 1, aux, to);
    }
}

int main()
{
    rHanoi(4, 'A', 'B', 'C');
}
/*
1개의 원판을 A에서 B로 옮긴다.
2개의 원판을 A에서 B로 옮긴다.
1개의 원판을 B에서 C로 옮긴다.
3개의 원판을 A에서 C로 옮긴다.
1개의 원판을 C에서 A로 옮긴다.
2개의 원판을 C에서 A로 옮긴다.
1개의 원판을 A에서 B로 옮긴다.
4개의 원판을 A에서 B로 옮긴다.
1개의 원판을 B에서 C로 옮긴다.
2개의 원판을 B에서 C로 옮긴다.
1개의 원판을 C에서 A로 옮긴다.
3개의 원판을 B에서 A로 옮긴다.
1개의 원판을 A에서 B로 옮긴다.
2개의 원판을 A에서 B로 옮긴다.
1개의 원판을 B에서 C로 옮긴다.
*/