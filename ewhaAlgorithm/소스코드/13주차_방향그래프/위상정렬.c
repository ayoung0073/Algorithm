// DFS 코드 참고
// 정점의 진입차수 위상 정렬
#include <stdio.h>
#include <stdlib.h>

typedef struct Edge
{
    int vNum1; // 정점번호 참고할 수 있도록
    int vNum2;
    struct Edge* next; // Edge를 위한 연결리스트 생성
    // 가중치를 넣을 수도 있음
}Edge;

typedef struct IncidentEdge
{
    int adjVertex; // 인접 정점 이름 
    Edge* e; // 간선과 연결
    struct IncidentEdge* next;
}IncidentEdge;

typedef struct Vertex
{
    int num; // 정점 번호
    int isFresh; // 필요 X
    struct Vertex* next;
    IncidentEdge* top; 
}Vertex;

Vertex* vHead = NULL;
Edge* eHead = NULL;
int vCount; // 정점 개수
int eCount; 
int in[6];

#define N 10

typedef struct 
{
    int element[N];
    int front, rear;
}Queue; // 원형 큐, 간단하게 배열로

void initQueue(Queue* Q)
{
    Q->front = 0;
    Q->rear = 0;
}

int isEmpty(Queue* Q)
{
    return Q->rear == Q->front;
}

int isFull(Queue* Q)
{
    return (Q->rear+1) % N == Q->front;
}

void enqueue(Queue* Q, char elem)
{
    if (isFull(Q))
    {
        printf("FULL\n");
        return;
    }
    Q->rear = (Q->rear + 1) % N;
    Q->element[Q->rear] = elem;
}

int dequeue(Queue* Q)
{
    if (isEmpty(Q))
    {
        printf("EMPTY\n");
        return 0;
    }
    Q->front = (Q->front + 1) % N;
    return Q->element[Q->front];
}

void makeVertices() // 정점 만드는 함수 // 정점을 만들어주고, 정점들 사이에 간선 부착하는 식으로.
{
    Vertex* p = (Vertex*)malloc(sizeof(Vertex));
    p->num = ++vCount; // 쉽게..
    p->top = NULL;
    p->next = NULL;
    p->isFresh = 0;
    Vertex* q = vHead; // q를 헤드로 넣음

    if (q == NULL) // 연결리스트 비어있는 경우
        vHead = p;
    else
    {
        while (q->next != NULL)
            q = q->next;
        q->next = p; // 마지막 정점 뒤에 정점 삽입
    }
}

Vertex* findVertex(int v)
{
    Vertex* p = vHead;
    while (p->num != v)
        p = p->next;
    return p;
}

void insertIncidentEdge(Vertex* v, int av, Edge* e)
{
    IncidentEdge* p = (IncidentEdge*)malloc(sizeof(IncidentEdge));
    p->adjVertex = av;
    p->e = e;
    p->next = NULL;
    IncidentEdge* q = v->top;
    if (q == NULL)
        v->top = p; // Head 역할이 top이오
    else
    {
        while (q->next != NULL)
            q = q->next;
        q->next = p;
    }
}

void insertEdges(int v1, int v2) // 파라미터 : 정점의 이름
{
    Edge* p = (Edge*)malloc(sizeof(Edge));
    p->vNum1 = v1;
    p->vNum2 = v2;
    p->next = NULL;
    Edge* q = eHead;

    if (q == NULL)
        eHead = p;
    else
    {
        while (q->next != NULL)
            q = q->next;
        q->next = p;
    }

    // 정점과 간선 사이에 인접 간선들을 연결해줘야 함.
    Vertex* v = findVertex(v1); // 주어진 정점의 위치를 리턴받아 그 정점과 만들어진 간선을 IncidentEdge로 연결시켜주는 메서드
    // v는 v1이고,, v1의 인접 정점은 v2,, v와 v2
    insertIncidentEdge(v, v2, p);

    // v = findVertex(v2); // 주어진 정점의 위치를 리턴받아 그 정점과 만들어진 간선을 IncidentEdge로 연결시켜주는 메서드
    // insertIncidentEdge(v, v1  , p);
}

void inDegree()
{
    Vertex* p = vHead;
    IncidentEdge* q;
    for (; p != NULL; p = p->next)
        for (q = p->top; q != NULL; q = q->next)
            in[q->adjVertex - 1]++;
}

void topologicalSort()
{
    Queue q;
    initQueue(&q);

    Vertex* p;
    IncidentEdge* r;
    inDegree(); // 진입 차수 구함

    for (int i = 0; i < 6; i++)
        if (in[i] == 0)
            enqueue(&q, i + 1);
    
    while (!isEmpty(&q))
    {
        int w = dequeue(&q);
        printf("[%d] ", w);
        p = findVertex(w);
        r = p->top;
        while (r != NULL)
        {
            in[r->adjVertex - 1]--;
            if (in[r->adjVertex - 1] == 0)
                enqueue(&q, r->adjVertex);
            r = r->next;
        }
    }

}

void print()
{
    Vertex* p = vHead;
    IncidentEdge* q;
    for (; p != NULL; p = p->next)
    { 
        printf("정점 %d : ", p->num); 
        for (q = p->top; q != NULL; q = q->next)
            printf("[%d] ", q->adjVertex);
        printf("\n");
    }
}

int main()
{
    for (int i = 0; i < 6; i++)
        makeVertices();

    insertEdges(1, 2);
    insertEdges(1, 5);
    insertEdges(2, 3);
    insertEdges(4, 5);
    insertEdges(5, 2);
    insertEdges(5, 3);
    insertEdges(5, 6);
    insertEdges(6, 3);


    print();

    topologicalSort();
    /* 나가는 지점으로
    정점 1 : [2] [5] 
    정점 2 : [3] 
    정점 3 : 
    정점 4 : [5] 
    정점 5 : [2] [3] [6] 
    정점 6 : [3] 

    [1] [4] [5] [2] [6] [3]
    */
    return 0;
}
  