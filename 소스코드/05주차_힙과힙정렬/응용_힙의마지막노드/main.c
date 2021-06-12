#include <stdio.h>
#include <stdlib.h>

#define MAX_SIZE 100

typedef struct StackType // 스택 구현
{ 
	int data[MAX_SIZE];
	int top;
}Stack;

typedef struct HeapType // 힙 구현
{ 
    int heap[MAX_SIZE];
    int heap_size;
}Heap;

/*
    스택 관련 함수
*/
void initStack(Stack* s)  // 스택 초기화
{
	s->top = -1; //포인터변수 s가 가리키는 top을 -1로 저장. 아직 stack에 아무것도 없다는 뜻
}

int isFull(Stack *s) // 스택 다 찼는지 확인
{
	return (s->top == (MAX_SIZE-1));
}

int isEmpty(Stack* s) // 스택 비었는지 확인
{
	return (s->top == -1);
}

void push(Stack* s, int data) 
{
	if (isFull(s)) 
    { // 최대 크기인 경우에는 error
		printf("Overflow\n");
		exit(1); // 비정상 종료
	}
	else s->data[++(s->top)] = data; // s가 가리키는 top을 1 증가 시킨후, 그 위치에 원소 저장
}

int pop(Stack* s) 
{
	if (isEmpty(s)) 
    { // 스택이 비어있으면 error
		printf("Stack is empty\n");
		exit(1); 
	}
	else return s->data[(s->top)--];
}

/*
    힙 관련 함수
*/
void initHeap(Heap* h) // 힙 초기화
{
    h->heap_size = 0;
}

void upHeap(Heap* h) 
{
    int i = h->heap_size;
    int key = h->heap[i];

    while ((i != 1) && h->heap[i / 2] > key) // 루트인지 확인 && 부모의 키값과 비교
    {
        h->heap[i] = h->heap[i / 2];
        i /= 2;
    }

    h->heap[i] = key;
}

void printHeap(Heap* h)
{
    for (int i = 1; i <= h->heap_size; i++)
        printf("[%d] ", h->heap[i]);
    printf("\n");
}

void insertItem(Heap* h, int key)
{
    h->heap_size++;
    h->heap[h->heap_size] = key;

    upHeap(h); // upHeap 함수 호출ㄴ
}

Stack* binaryExpansion(int i, Stack* s)
{
    while (i >= 2)
    {
        push(s, i % 2);
        i /= 2;
    }
    push(s, i);

    return s;
}

int findLastNode(Heap* h)
{
    Stack s;
    int bit;
    initStack(&s);
    int v = 1; // 루트 노드

    binaryExpansion(h->heap_size, &s);
    pop(&s); 

    while (!isEmpty(&s))
    {
        bit = pop(&s);
        if (bit == 0)
            v = v * 2;
        else
            v = v * 2 + 1;
    }

    return h->heap[v];
}

int main()
{
    Heap heap;
    initHeap(&heap);

    // insert 함수 실행
    insertItem(&heap, 14);
    insertItem(&heap, 2);
    insertItem(&heap, 4);
    insertItem(&heap, 7);
    insertItem(&heap, 9);
    insertItem(&heap, 8);
    insertItem(&heap, 6);
    insertItem(&heap, 15);
    insertItem(&heap, 17);
    insertItem(&heap, 12);
    insertItem(&heap, 13);

    printHeap(&heap);

    printf("힙의 마지막 노드 : %d\n", findLastNode(&heap));

    return 0;
}

