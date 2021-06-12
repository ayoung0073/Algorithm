#include <stdio.h>
#include <stdlib.h>

typedef struct QueueNode
{
    int data;
    struct QueueNode* link;
}QueueNode;

typedef struct
{
    QueueNode* front;
    QueueNode* rear;
}LinkedQueue;

void init(LinkedQueue* queue)
{
    queue->front = queue->rear = NULL;
}

int is_empty(LinkedQueue* queue)
{
    return queue->front == NULL;
}

void enqueue(LinkedQueue* queue, int data)
{
    QueueNode* temp = (QueueNode*)malloc(sizeof(QueueNode));
    temp->data = data;
    temp->link = NULL;
    if(is_empty(queue)) // queue가 비어있는 경우
    {
        queue->front = temp;
        queue->rear = temp;
    }
    else
    {
        queue->rear->link = temp;
        queue->rear = temp;
    }
}

int dequeue(LinkedQueue* queue)
{
    QueueNode* temp = queue->front; // dequeue할 노드
    int data;
    if(is_empty(queue))
    {
        fprintf(stderr, "Queue is empty\n");
        exit(1);
    }
    else
    {
        data = temp->data; // 리턴값
        queue->front = temp->link;
        if(queue->front == NULL) // 전체 큐의 노드가 1개뿐인 경우 : 더이상 아무것도 없
            queue->rear = NULL; // queue->rear 은 temp를 가리키고 있기 때문에 queue->rear도 NULL 처리를 해줘야 한다.
        free(temp);
        return data;
    }
}

void print_queue(LinkedQueue* queue)
{
    QueueNode* p;
    for(p = queue->front; p != NULL; p = p->link)
        printf("|%d| -> ", p->data);
    printf("|NULL|\n");
}

int main()
{
    LinkedQueue queue;
    init(&queue);
    
    enqueue(&queue, 10); print_queue(&queue);
    enqueue(&queue, 20); print_queue(&queue);
    enqueue(&queue, 30); print_queue(&queue);
    getchar();
    
    dequeue(&queue); print_queue(&queue);
    dequeue(&queue); print_queue(&queue);
    dequeue(&queue); print_queue(&queue);

    return 0;
}
/*
|10| -> |NULL|                                                                                                                          
|10| -> |20| -> |NULL|                                                                                                                  
|10| -> |20| -> |30| -> |NULL|                                                                                                          
                                                                                                                                        
|20| -> |30| -> |NULL|                                                                                                                  
|30| -> |NULL|                                                                                                                          
|NULL|
*/
