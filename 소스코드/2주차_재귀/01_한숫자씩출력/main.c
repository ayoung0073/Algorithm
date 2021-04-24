#include <stdio.h>
#include <stdlib.h>

void rPrintDigits(int n)
{
    if(n < 10) // 단자리 수인 경우(재귀 함수 종료 조건)
        printf("%d\n", n);
    else 
    {
        rPrintDigits(n / 10); // 재귀 호출(앞자리 숫자들이 파라미터(3408 : 340 -> 34 -> 3))
        printf("%d\n", n % 10);
    }
}

void printDigits() // 간접 재귀 함수
{
    int n;
    printf("Enter a number : "); 
    scanf("%d", &n);
    if (n < 0)
        printf("Negative!\n");
    else
        rPrintDigits(n);
}

void main()
{
    printDigits();
}