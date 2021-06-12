#include <stdio.h>

#define SIZE 6

void spans(int X[], int S[])
{
    int s;
    for(int i = 0; i < SIZE; i++)
    {
        s = 1;
        while ((s <= i) && (X[i - s] <= X[i]))
            s++;
        S[i] = s;
    }
}

int main()
{
    int X[SIZE] = {6, 3, 4, 2, 5, 3};
    int S[SIZE] = {0};
    
    spans(X, S);
    
    for (int i = 0; i < SIZE; i++)
        printf(" [%d] ", S[i]);
    printf("\n");

    return 0;
}
/*
[1]  [1]  [2]  [1]  [4]  [1]
*/