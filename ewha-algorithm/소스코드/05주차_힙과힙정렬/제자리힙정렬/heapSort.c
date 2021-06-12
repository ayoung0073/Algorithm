#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define MAX_ELEMENT 32

typedef struct
{
    int heap_[MAX_ELEMENT];
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
   int key = h->heap_[i];

   while ((i != 1) && (key < h->heap_[i / 2])) // 1, 2 동시 확인(반복)
   {
       // SWAP 진행
       h->heap_[i] = h->heap_[i / 2]; // 이미 key를 저장해놓은 상태라서 바로 바꿀 수 있음
       i /= 2;
   }
   h->heap_[i] = key;
}

void downHeap(HeapType* h)
{
    int temp = h->heap_[1];
    int parent = 1, child = 2; // parent, child : 위치

    while(child <= h->heap_size) // down 할 수 있는 조건
    {
        if((child < h->heap_size) && (h->heap_[child] > h->heap_[child + 1])) // 내 오른쪽에 노드가 있는 경우
            child++;
        if(temp <= h->heap_[child]) // SWAP 할 필요 없는 경우
            break;
        h->heap_[parent] = h->heap_[child];
        parent = child;
        child *= 2;
    }
    h->heap_[parent] = temp;
}

void insertItem(HeapType* h, int key)
{
    h->heap_size++;
    h->heap_[h->heap_size] = key;
    // upHeap 함수 호출
    upHeap(h);
}

int removeMin(HeapType* h)
{
    int key = h->heap_[1]; 
    h->heap_[1] = h->heap_[h->heap_size]; // 루트노드에 라스트노드 저장
    h->heap_size--;
    // downHeap 함수 호출
    downHeap(h);
    return key;
}

void printHeap(HeapType* h)
{
    for (int i = 1; i <= h->heap_size; i++)
        printf("[%d] ", h->heap_[i]);
    printf("\n");
}

void printArray(int list[], int n)
{
    for(int i = 1; i <= n; i++)
        printf("[%d] ", list[i]);
    printf("\n");
} 

void inPlaceHeapSort(HeapType* h) // 제자리 힙 정렬
{
    int size = h->heap_size;
    int key; // 기억할 변수 선언
    for (int i = 0; i < size; i++)
    {
        key = removeMin(h);
        h->heap_[h->heap_size + 1] = key;
    }
}

int main() 
{
    HeapType heap;
    srand(time(NULL));
    init(&heap);
    printf("%d\n\n\n", heap.heap_[0]);
    for (int i = 0; i < 15; i++)
        insertItem(&heap, rand() % 100);
    for (int i = 1; i <= 15; i++)
        printf("[%d] ", heap.heap_[i]);
    printf("\n");
    printHeap(&heap);
    getchar();
    inPlaceHeapSort(&heap); // 내림차순 정렬
    // printHeap(&heap)

    for (int i = 1; heap.heap_[i] > 0; i++)
        printf("[%d] ", heap.heap_[i]);
}