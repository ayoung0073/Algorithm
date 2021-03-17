#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int iter_power(int x, int n)
{
    int result = 1;
    for (int i = 0; i < n; i++)
        result *= x;
    return result;
}

int recur_power(int x, int n) // 시간 복잡도 O(log2N)
{
    if(n == 0)
        return 1;
    else if ((n % 2) == 0) // 짝수인 경우
        return recur_power(x * x, n / 2); // n이 작아지도록
    else // 홀수인 경우
        return x * recur_power(x * x, (n - 1) / 2);
}   

void main()
{
    float start = clock();
    printf("2 ^ 10 = %d\n", iter_power(2, 10));
    float end = clock();
    
    printf("%f\n", end - start);
    start = clock();
    printf("2 ^ 10 = %d\n", recur_power(2, 10));
    end = clock();
    printf("%f\n", end - start); 
}