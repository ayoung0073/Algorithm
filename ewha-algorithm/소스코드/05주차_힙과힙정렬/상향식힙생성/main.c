#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define MAX_ELEMENT 100

struct Heap
{
    int H[MAX_ELEMENT];
    int n;
}_Heap;

void downHeap(int i) // 파라미터 : 인덱스
{
    if(i * 2 > _Heap.n) return;
    if (_Heap.H[i] < _Heap.H[i * 2] || _Heap.H[i] < _Heap.H[i * 2 + 1])
    {
        if (_Heap.H[i * 2] > _Heap.H[i * 2 + 1]) // 왼쪽 노드가 오른쪽 노드보다 큰 경우
        {
            int temp;
            temp = _Heap.H[i];
            _Heap.H[i] = _Heap.H[i * 2];
            _Heap.H[i * 2] = temp;
            downHeap(i * 2); // 해당 자식노드 재귀호출
        }

        else
        {
            int temp;
            temp = _Heap.H[i];
            _Heap.H[i] = _Heap.H[i * 2 + 1];
            _Heap.H[i * 2 + 1] = temp;
            downHeap(i * 2 + 1); // 자식 재귀호출
        }
    }
    else return;
}

void buildHeap() // 비재귀적 상향식 힙생성
{
    for (int i = _Heap.n / 2; i >= 1; i--)
        downHeap(i);
}

void rBuildHeap(int i)
{
    if (i > _Heap.n) return;
    if (i * 2 <= _Heap.n) rBuildHeap(2 * i);
    if (i * 2 + 1 <= _Heap.n) rBuildHeap(2 * i + 1);

    downHeap(i);
}

int removeMax()
{
    int key = _Heap.H[1];
    _Heap.H[1] = _Heap.H[_Heap.n--]; // 마지막 인덱스를 첫번째 인덱스에 저장
    downHeap(1);

    return key;
}

void inPlaceHeapSort() // 제자리 힙정렬
{
    int size = _Heap.n;
    int key;
    for (int i = 0; i < size; i++)
    {
        key = removeMax();
        _Heap.H[_Heap.n + 1] = key; 

    }
}

void printHeap()
{
    for (int i = 1; i <= _Heap.n; i++)
        printf("[%d] ", _Heap.H[i]);
    printf("\n");
}

void printArray() // n이 0이기 때문에 다른 조건으로 출력
{
    for (int i = 1; _Heap.H[i] > 0; i++)
        printf("[%d] ", _Heap.H[i]);
    printf("\n");
}

int main()
{
    _Heap.n = 0;
    srand(time(NULL));
    printf("입력할 원소의 개수 : ");
    scanf("%d", &_Heap.n);
    for (int i = 1; i <= _Heap.n; i++)
        _Heap.H[i] = rand() % 100;

    // buildHeap(); // 힙생성
    rBuildHeap(1);
    printHeap();

    getchar();

    inPlaceHeapSort();
    printArray();

    return 0;
}