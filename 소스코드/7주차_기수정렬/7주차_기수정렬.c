#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define MAX_SIZE 15
#define BUCKETS 10
#define DIGITS 2

typedef int element;
typedef struct
{
    element data[MAX_SIZE];
    int front, rear;
}QueueType; // 원형 큐

void init_queue(QueueType* q)
{
    q->front = q->rear = 0;
}

int is_empty(QueueType* q)
{
    return q->front == q->rear;
}

int is_full(QueueType* q)
{
    return (q->rear + 1) % MAX_SIZE == q->front;
}

void enqueue(QueueType* q, element item)
{
    if (is_full(q)) exit(1);
    
    q->rear = (q->rear + 1) % MAX_SIZE;
    q->data[q->rear] = item;
}

element dequeue(QueueType* q)
{
    if (is_empty(q)) exit(1);
    
    q->front = (q->front + 1) % MAX_SIZE;
    return q->data[q->front];
}

void print_queue(QueueType* q)
{
    if (!is_empty(q))
    {
        int i = q->front;
        do
        {
            i = (i + 1) % MAX_SIZE;
            printf("%d | ", q->data[i]);
            if(i == q->rear) break;
        }while(i != q->front);
    }
    printf("\n");
}

void print_buckets(QueueType queues[])
{
    printf("\n=====================\n");
    
    for (int b = 0; b < BUCKETS; b++)
    {
        printf("[%d] -> ", b);
        print_queue(&queues[b]);
    }
    printf("\n=====================\n");
}


void radix_sort(int list[], int n)
{
    int i, b, d, factor = 1; // 첫째 자리부터
    QueueType queues[BUCKETS];
    
    for (b = 0; b < BUCKETS; b++)
        init_queue(&queues[b]); // 큐 초기화
    
    for (d = 0; d < DIGITS; d++)
    {
        for (i = 0; i < n; i++)
            enqueue(&queues[(list[i] / factor) % 10], list[i]);
            
        print_buckets(queues);
        
        for (b = i = 0; b < BUCKETS; b++)
            while (!is_empty(&queues[b]))
                list[i++] = dequeue(&queues[b]);
        factor *= 10; // 다음 자리 정렬
    }
}

int main()
{
    int list[MAX_SIZE];
    srand(time(NULL));
    
    for(int i = 0; i < MAX_SIZE; i++)
        list[i] = rand() % 100;
    
    for (int i = 0; i < MAX_SIZE; i++)
        printf("[%d] ", list[i]);
    printf("\n\n");
    
    radix_sort(list, MAX_SIZE);
    
    for (int i = 0; i < MAX_SIZE; i++)
        printf("[%d] ", list[i]);
    printf("\n\n");
    
    return 0;
}

/*
[94] [39] [68] [75] [83] [33] [84] [30] [16] [82] [31] [0] [61] [83] [43] 


=====================
[0] -> 30 | 0 | 
[1] -> 31 | 61 | 
[2] -> 82 | 
[3] -> 83 | 33 | 83 | 43 | 
[4] -> 94 | 84 | 
[5] -> 75 | 
[6] -> 16 | 
[7] -> 
[8] -> 68 | 
[9] -> 39 | 

=====================

=====================
[0] -> 0 | 
[1] -> 16 | 
[2] -> 
[3] -> 30 | 31 | 33 | 39 | 
[4] -> 43 | 
[5] -> 
[6] -> 61 | 68 | 
[7] -> 75 | 
[8] -> 82 | 83 | 83 | 84 | 
[9] -> 94 | 

=====================
[0] [16] [30] [31] [33] [39] [43] [61] [68] [75] [82] [83] [83] [84] [94] 
*/