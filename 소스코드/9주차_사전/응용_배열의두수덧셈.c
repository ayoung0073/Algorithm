 #include <stdio.h>
 #include <stdlib.h>

 #define SIZE 8

 typedef struct 
 {
     int elem;
     int idx;   
 }Dict;

void sort(Dict D[])
{
    int elem, i, j, idx;
    for (i = 1; i < SIZE; i++)
    {
        elem = D[i].elem;
        idx = D[i].idx;
        for (j = i - 1; j >= 0 && D[j].elem > elem; j--)
            D[j + 1] = D[j];
        D[j + 1].elem = elem;
        D[j + 1].idx = idx;
    }
}

int findElement(Dict D[], int v)
{
    int left = 0;
    int right = SIZE - 1;
    int mid;

    while (left < right)
    {
        mid = (left + right) / 2;
        if (v == D[mid].elem)
            return D[mid].idx;
        else if (v > D[mid].elem)
            left = mid + 1;
        else
            right = mid - 1;
    }
    return -1;
}

void findIndexPair(Dict D[], int A[], int s)
{
    int j;
    for (int i = 0; i < SIZE; i++)
    {
        int v = s - A[i];
        j = findElement(D, v); // 이진탐색으로 찾기
        if (j != -1)
        {
            printf("FindElement : A[%d] = %d, A[%d] = %d\n", i, A[i], j, A[j]);
            return;
        }
    }
    if (j == -1)
        printf("Not Found\n");
}

void buildDict(Dict D[], int A[])
{
    for (int i = 0; i < SIZE; i++)
    {
        D[i].elem = A[i];
        D[i].idx = i;
    }
    sort(D);
}

int main()
{
    int A[SIZE] = {2, 21, 8, 3, 5, 1, 13, 1};
    Dict D[SIZE];
    
    buildDict(D, A); // 순서사전 만들기
    for (int i = 0; i < SIZE; i++)
        printf("(%d, %d) ", D[i].elem, D[i].idx);
    printf("\n");
    printf("합을 입력하세요 : ");
    int num;
    scanf("%d", &num);
    findIndexPair(D, A, num);
    return 0;
}
 