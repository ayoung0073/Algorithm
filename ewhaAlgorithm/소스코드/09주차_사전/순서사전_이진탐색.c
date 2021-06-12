#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#define SIZE 15

typedef struct
{
    int key;
    char value[10];
}element;

typedef struct
{
    element dict[SIZE];
    int size;
}DictType;

void init(DictType* d)
{
    d->size = 0;
}

void insertKey(DictType* d)
{
    for (int i = 0; i < SIZE; i++)
    {
        d->dict[i].key = rand() % 30 + 1;
        for (int j = 0; j < i; j++)
            if (d->dict[i].key == d->dict[j].key)
                i--;
    }
}

void insertValue(DictType* d)
{
    for (int i = 0; i < SIZE; i++)
    {
        for (int j = 0; j < 5; j++)
            d->dict[i].value[j] = rand() % 26 + 97;
        d->size++;
    }
}

void makeDict(DictType* d)
{
    insertKey(d);
    insertValue(d);
}

void insertion_sort(DictType* d)
{
    int i, j;
    element item;
    for (i = 1; i < SIZE; i++)
    {
        item = d->dict[i];
        for (j = i - 1; j >= 0; j--)
        {
            if (d->dict[j].key > item.key)
                d->dict[j + 1] = d->dict[j];
            else
                break;
        }
        
        // for (j = i - 1; j  >= 0 && d->dict[j].key > item.key; j--)
        //         d->dict[j + 1] = d->dict[j];
        
        d->dict[j + 1] = item;
    }
}

int rFindElement(DictType* d, int key, int l, int r) // 이진탐색 재귀함수
{
    int mid;
    if(l <= r)
    {
        mid = (l + r) / 2;
        if (key == d->dict[mid].key)
            return mid;
        else if (key < d->dict[mid].key)
            return rFindElement(d, key, l, mid - 1);
        else
            return rFindElement(d, key, mid + 1, r);
    }
    return -1;
}

int findElement(DictType* d, int key, int l, int r) // 반복문
{
    int mid;
    while (l <= r)
    {
        mid = (l + r) / 2;
        if (key == d->dict[mid].key)
            return mid;
        else if (key < d->dict[mid].key)
            r = mid - 1;
        else
            l = mid + 1;
    }
    return -1;
}

void removeElement(DictType* d, int key)
{
    int index = findElement(d, key, 0, d->size - 1);
    if (index == -1)
    {
        printf("삭제할 요소가 없습니다.\n");
        return;
    }
    else
    {
        element item = d->dict[index];
        for (int i = index; i < d->size - 1; i++)
            d->dict[i] = d->dict[i + 1];
        d->size--;
        return;
    }
}

void printDict(DictType* d)
{
    printf("key  value \n==========\n");
    for (int i = 0; i < d->size; i++)
    {
        printf("%2d  ", d->dict[i].key);
        for (int j = 0; j < 5; j++)
            printf("%c", d->dict[i].value[j]);
        printf("\n");
    }
}

int main()
{
    DictType d;
    init(&d);
    srand(time(NULL));
    makeDict(&d);
    printDict(&d); 

    getchar();

    printf("\n");
    insertion_sort(&d);
    printDict(&d);

    getchar();

    printf("\n검색할 키값을 입력 : ");
    int key;
    scanf("%d", &key);
    int index = findElement(&d, key, 0, SIZE - 1);
    // int index = rFindElement(&d, key, 0, SIZE - 1);
    if (index == -1)
        printf("\n검색에 실패하였습니다.\n");
    else
    {
        printf("\n위치 %d에서 키 : %d, 값 : '", index + 1, key);
        for (int j = 0; j < 5; j++)
            printf("%c", d.dict[index].value[j]);
        printf("'이 검색되었습니다.\n");
    }

    printf("\n삭제할 키값을 입력 : ");
    scanf("%d", &key);
    removeElement(&d, key);
    printDict(&d);

    return 0;
}

/*
key  value 
==========
13  afdxq
23  leyzt
27  dogad
20  booeh
16  fcile
 2  ihgic
 9  hjwkk
30  onokp
 4  pdpkz
17  hvquv
19  mdzed
 1  zpaky
24  dqxhk
 3  jcddb
22  mhurj


key  value 
==========
 1  zpaky
 2  ihgic
 3  jcddb
 4  pdpkz
 9  hjwkk
13  afdxq
16  fcile
17  hvquv
19  mdzed
20  booeh
22  mhurj
23  leyzt
24  dqxhk
27  dogad
30  onokp


검색할 키값을 입력 : 23

위치 12에서 키 : 23, 값 : 'leyzt'이 검색되었습니다.

삭제할 키값을 입력 : 23
key  value 
==========
 1  zpaky
 2  ihgic
 3  jcddb
 4  pdpkz
 9  hjwkk
13  afdxq
16  fcile
17  hvquv
19  mdzed
20  booeh
22  mhurj
24  dqxhk
27  dogad
30  onokp
*/