// 가중치 조건 추가
#include <stdio.h>
#include <stdlib.h>

#define N 5
#define INF 10000

typedef struct Edge
{
    int vNum1;
    int vNum2;
    int weight;
    struct Edge* next;
}Edge;

typedef struct IncidentEdge
{
    int adjVertex;
    int weight;
    Edge* e; 
    struct IncidentEdge* next;
}IncidentEdge;

typedef struct Vertex
{
    int num; // 정점 번호
    int isFresh;
    struct Vertex* next;
    IncidentEdge* top; 
}Vertex;

Vertex* vHead = NULL;
Edge* eHead = NULL;
int vCount; // 정점 개수
int eCount; 
int dist[N]; // 배낭의 역할

void makeVertices() // 정점 만드는 함수 // 정점을 만들어주고, 정점들 사이에 간선 부착하는 식으로.
{
    Vertex* p = (Vertex*)malloc(sizeof(Vertex));
    p->num = ++vCount; 
    p->top = NULL;
    p->next = NULL;
    p->isFresh = 0;
    Vertex* q = vHead; 

    if (q == NULL) 
        vHead = p;
    else
    {
        while (q->next != NULL)
            q = q->next;
        q->next = p; 
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
    p->weight = e->weight;
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

void insertEdges(int v1, int v2, int w) // w: weight 
{
    Edge* p = (Edge*)malloc(sizeof(Edge));
    p->vNum1 = v1;
    p->vNum2 = v2;
    p->weight = w;
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

    v = findVertex(v2); // 주어진 정점의 위치를 리턴받아 그 정점과 만들어진 간선을 IncidentEdge로 연결시켜주는 메서드
    insertIncidentEdge(v, v1, p);
}

int getMinVertex()
{
    int v;
    Vertex* p = vHead;
    for (; p != NULL; p = p->next)
        if (p->isFresh == 0)
        {
            v = p->num - 1; // 처음에 v에는 0이 들어가있을 것
            break;
        }
    
    for (p = vHead; p != NULL; p = p->next) // Fresh인 것 중에 찾음.
        if (p->isFresh == 0 && (dist[p->num - 1] < dist[v]))
            v = p->num - 1;

    return v;
}

void prim(Vertex* v)
{
    IncidentEdge* q;
    Vertex* p;
    int u; // 정점 번호 기억

    for (int i = 0; i < N; i++)
        dist[i] = INF;
    
    dist[v->num - 1] = 0; // 0 번 인덱스부터 저장

    for (int i = 0; i < N; i++)
    {
        u = getMinVertex(); // 처음엔 시작점으로 나올 것 정점 번호로 나옴(근데 index여서 다음 코드 (+1) 처리한 것)
        p = findVertex(u + 1); // 정점 번호가 u + 1 인 정점 노드를 찾는다.
        p->isFresh = 1;
        printf("[%d] ", p->num);
        printf("인접 테스트 : ");
        for (q = p->top; q != NULL; q = q->next)
        {
            p = findVertex(q->adjVertex);
            printf("[%d] ", p->num);
            dist[q->adjVertex - 1] = q->weight;
        }
        printf("\n");
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
            printf("[%d (%d)] ", q->adjVertex, q->weight);
        printf("\n");
    }
}

int main()
{
    for (int i = 0; i < N; i++)
        makeVertices();

    insertEdges(1, 2, 1);
    insertEdges(1, 4, 2);
    insertEdges(1, 5, 4);
    insertEdges(2, 3, 6);
    insertEdges(2, 5, 7);
    insertEdges(3, 5, 5);
    insertEdges(4, 5, 3);

    print();
    prim(vHead); // [1] [2] [4] [5] [3] 
    // prim(vHead->next); // [2] [1] [4] [5] [3] 

    return 0;
}

/*
정점 1 : [2 (1)] [4 (2)] [5 (4)] 
정점 2 : [1 (1)] [3 (6)] [5 (7)] 
정점 3 : [2 (6)] [5 (5)] 
정점 4 : [1 (2)] [5 (3)] 
정점 5 : [1 (4)] [2 (7)] [3 (5)] [4 (3)] 
*/
  