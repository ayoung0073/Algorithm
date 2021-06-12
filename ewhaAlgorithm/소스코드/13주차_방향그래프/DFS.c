#include <stdio.h>
#include <stdlib.h>

typedef struct Edge
{
    int vNum1; // 정점번호 참고할 수 있도록
    int vNum2;
    int isTree; // 트리 back을 알기 위한 변수(쓰진 않을 예정) 
    struct Edge* next; // Edge를 위한 연결리스트 생성

    // 가중치를 넣을 수도 있음
}Edge;

typedef struct IncidentEdge
{
    int adjVertex; // 인접 정점 이름 (opposite 함수 필요없게끔)
    Edge* e;
    struct IncidentEdge* next;
}IncidentEdge;

typedef struct Vertex
{
    int num; // 정점 번호
    int isFresh;
    struct Vertex* next;
    IncidentEdge* top; 
    // 전체적인 코드 쉬워지도록 // 정점별 인접 간선들
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

void insertIncidentEdge(Vertex* v, int av, Edge* e) // (정점노드, 정수, 간선노드)
{
    IncidentEdge* p = (IncidentEdge*)malloc(sizeof(IncidentEdge));
    p->adjVertex = av;
    p->e = e;
    p->next = NULL;
    IncidentEdge* q = v->top;
    if (q == NULL)
        v->top = p; // Head 역할이 top이다.
    else
    {
        while (q->next != NULL)
            q = q->next;
        q->next = p;
    }
}

void insertEdges(int v1, int v2) // 파라미터 : 정점의 이름
{
    Edge* p = (Edge*)malloc(sizeof(Edge)); // 간선 생성
    p->vNum1 = v1;
    p->vNum2 = v2;
    p->isTree = 0; // fresh 해주기 위해
    p->next = NULL;
    // 아직 간선인접리스트에 넣진 않음. 생성만 진행.

    Edge* q = eHead; // 임시로 헤드 저장 (while문을 통해 마지막 노드로 저장할 것.)

    if (q == NULL)
        eHead = p; // 아직 간선인접리스트가 비어있다면 해당 노드로 설정
    else
    {
        while (q->next != NULL)
            q = q->next;
        q->next = p; // 마지막 노드로 삽입
    }

    // 정점과 간선 사이에 인접 간선들을 연결해줘야 함.
    Vertex* v = findVertex(v1); 
    // 주어진 정점의 위치를 리턴받아 그 정점과  
    // 만들어진 간선을 IncidentEdge로 연결시켜주는 메서드
    // v는 v1이고, v1의 인접 정점은 v2, v와 v2
    insertIncidentEdge(v, v2, p);
    // insertIncidentEdge(v, v1, p);
}

void dfs(Vertex* v)
{
    IncidentEdge* q;
    if (v->isFresh == 0) // 처음인 경우 방문 기록
    {
        printf("[%d] ", v->num);
        v->isFresh = 1;
    }
    for (q = v->top; q != NULL; q = q->next)
    {
        v = findVertex(q->adjVertex); // 다음 정점
        if (v->isFresh == 0)
            dfs(v);
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
    for (int i = 0; i < 9; i++)
        makeVertices();

    insertEdges(1, 2); // 간선으로 정점을 이음 
    insertEdges(1, 3);
    insertEdges(2, 4);
    insertEdges(2, 5);
    insertEdges(3, 5);
    insertEdges(3, 6);
    insertEdges(4, 7);
    insertEdges(5, 7);
    insertEdges(5, 8);
    insertEdges(6, 8);
    insertEdges(7, 9);
    insertEdges(8, 9);

    print();

    dfs(vHead);
    
    return 0;
}
  
/*
    정점 1 : [2] [3] 
    정점 2 : [4] [5] 
    정점 3 : [5] [6] 
    정점 4 : [7] 
    정점 5 : [7] [8] 
    정점 6 : [8] 
    정점 7 : [9] 
    정점 8 : [9] 
    정점 9 : 
    [1] [2] [4] [7] [9] [5] [8] [3] [6] 
*/