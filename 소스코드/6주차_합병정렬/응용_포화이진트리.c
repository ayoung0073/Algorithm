#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <unistd.h>

#define MAX_SIZE 15
#define MAX(a, b) (((a) > (b)) ? (a) : (b))
#define MAX3(a,b,c) (((a)>(b)) ? ((a) > (c) ? (a) : (c)) : ((b) > (c) ? (b) : (c)))

typedef struct
{
    int heap[MAX_SIZE];
    int heap_size; // 마지막 위치
}HeapType;

void init(HeapType* h)
{
    h->heap_size = 0;
}

void insertItem(HeapType* h, int key)
{
    h->heap_size++; // 힙 재구성 전, 사이즈 먼저 늘리기
    h->heap[h->heap_size] = key;
}

int max1(HeapType* h, int n)
{
    if (n > h->heap_size) return 0;
    return h->heap[n] + MAX(max1(h, n * 2), max1(h, n * 2 + 1));
}

int max2(HeapType* h, int n)
{
    if (n > h->heap_size)
        return 0;
    if (n <= h->heap_size && n*2 > h->heap_size && n*2 + 1 > h->heap_size)
        return h->heap[n];
    printf("%d : +%d\n", n, h->heap[n]);
    return h->heap[n] + MAX3(max2(h, n*2), max2(h, n*2+1), max1(h, n*2) + max1(h, n*2+1));
}

void printHeap(HeapType* h)
{
    for (int i = 1; i <= h->heap_size; i++)
        printf("[%d] ", h->heap[i]);
    printf("\n");
}


int main()
{
    HeapType heap;
    init(&heap);

    // insert 함수 실행
    insertItem(&heap, 36);
    insertItem(&heap, 21);
    insertItem(&heap, 6);
    insertItem(&heap, 15);
    insertItem(&heap, 30);
    insertItem(&heap, 11);
    insertItem(&heap, 10);
    insertItem(&heap, 10);
    insertItem(&heap, 19);
    insertItem(&heap, 20);
    insertItem(&heap, 14);
    insertItem(&heap, 5);
    insertItem(&heap, 9);
    insertItem(&heap, 2);
    insertItem(&heap, 7);
    printHeap(&heap);

    printf("%d\n", max2(&heap, 1));

}