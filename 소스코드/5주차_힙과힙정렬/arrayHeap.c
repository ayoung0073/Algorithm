#include <stdio.h>
#include <stdlib.h>

#define MAX_ELEMENT 100

typedef struct
{
    int heap[MAX_ELEMENT];
    int heap_size; // 마지막 위치
}HeapType;

void init(HeapType* h)
{
    h->heap_size = 0;
}

void upHeap(HeapType* h)
{
    /*
    1. 루트인지 확인
    2. 부모의 키값과 비교
    */
   int i = h->heap_size;
   int key = h->heap[i];

   while ((i != 1) && (key < h->heap[i / 2])) // 1, 2 동시 확인(반복)
   {
       // SWAP 진행
       h->heap[i] = h->heap[i / 2]; // 이미 key를 저장해놓은 상태라서 바로 바꿀 수 있음
       i /= 2;
   }
   h->heap[i] = key;
}

void downHeap(HeapType* h)
{
    int temp = h->heap[1];
    int parent = 1, child = 2; // parent, child : 위치

    while(child <= h->heap_size) // down 할 수 있는 조건
    {
        if((child < h->heap_size) && (h->heap[child] > h->heap[child + 1])) // 내 오른쪽에 노드가 있는 경우
            child++;
        if(temp <= h->heap[child]) // SWAP 할 필요 없는 경우
            break;
        h->heap[parent] = h->heap[child];
        parent = child;
        child *= 2;
    }
    h->heap[parent] = temp;
}

void insertItem(HeapType* h, int key)
{
    h->heap_size++;
    h->heap[h->heap_size] = key;
    // upHeap 함수 호출
    upHeap(h);
}

int removeMin(HeapType* h)
{
    int key = h->heap[1]; 
    h->heap[1] = h->heap[h->heap_size]; // 루트노드에 라스트노드 저장
    h->heap_size--;
    // downHeap 함수 호출
    downHeap(h);
    return key;
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
    insertItem(&heap, 5);
    insertItem(&heap, 1);
    insertItem(&heap, 4);
    insertItem(&heap, 7);
    insertItem(&heap, 3);
    insertItem(&heap, 8);
    insertItem(&heap, 1);
    insertItem(&heap, 2);
    insertItem(&heap, 10);
    insertItem(&heap, 11);

    printHeap(&heap);

    printf("deleted key : %d\n", removeMin(&heap));
    
    printHeap(&heap);

    return 0;
}

// [1] [2] [1] [3] [5] [8] [4] [7] [10] [11] 