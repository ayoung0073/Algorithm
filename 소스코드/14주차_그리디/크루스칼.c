#include <stdio.h>
#include <stdlib.h>

#define N 7
#define SWAP(x, y, t) ((t) = (x), (x) = (y), (y) = (t))

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

Edge* e[14];

void printEdge()
{
    Edge* p = eHead;
    int i = 0;

    for (; p != NULL; p = p->next)
        e[i++] = p;

    int least;
    Edge* temp;
    for (i = 0; i < 13; i++)
    {
        least = i;
        for (int j = i + 1; j < 14; j++)
            if (e[j]->weight < e[least]->weight)
                least = j;
        SWAP(e[i], e[least], temp);
    }

    // for (i = 0; i < 14; i++)
    //     printf("[%d - %d (%d)] \n", e[i]->vNum1, e[i]->vNum2, e[i]->weight);
    // printf("\n");
}

int v[N]; // 집합 체크
void initSet()
{
    for (int i = 0; i < N; i++)
        v[i] = -1;
}

int vFind(int vNum)
{
    if (v[vNum] == -1)
        return vNum;
    while (v[vNum] != -1)
        vNum = v[vNum];
    return vNum;
}

void vUnion(int vNum1, int vNum2)
{
    int r1 = vFind(vNum1);
    int r2 = vFind(vNum2);

    if (r1 != r2)
        v[r2] = r1;
}

void kruskcal()
{
    int eCount = 0;
    int v1, v2;

    int i = 0;
    initSet();
    Edge* p;

    while (eCount < N)
    {
        p = e[i];
        v1 = vFind(p->vNum1 - 1);
        v2 = vFind(p->vNum2 - 1);

        if (v1 != v2)
        {
            printf("간선 [%d - %d (%d)] 선택\n", p->vNum1, p->vNum2, p->weight);
            eCount++;
            vUnion(v1, v2);
        }
        i++; // 다음 간선 확인
    }
}

int main()
{
    for (int i = 0; i < N; i++)
        makeVertices();

    insertEdges(1, 2, 10); insertEdges(1, 3, 15); insertEdges(1, 4, 8); insertEdges(1, 5, 27);
    insertEdges(2, 4, 25); insertEdges(2, 5, 4);
    insertEdges(3, 4, 13); insertEdges(3, 6, 32); insertEdges(3, 7, 8);
    insertEdges(4, 5, 10); insertEdges(4, 6, 19); insertEdges(4, 7, 22);
    insertEdges(5, 7, 25);
    insertEdges(6, 7, 15);

    // 정렬된 간선 출력
    printEdge(); 

    // 순차적으로 끄집어내서 연결.. + 사이클 발생하지 않도록 하자.
    kruskcal();
    /*
    간선 [2 - 5 (4)] 선택
    간선 [1 - 4 (8)] 선택
    간선 [3 - 7 (8)] 선택
    간선 [1 - 2 (10)] 선택
    간선 [3 - 4 (13)] 선택
    간선 [6 - 7 (15)] 선택
    */
    return 0;
}