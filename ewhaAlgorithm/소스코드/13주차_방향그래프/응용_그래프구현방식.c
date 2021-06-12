#include <stdio.h>
#include <stdlib.h>

#define N 10

typedef struct Vertex
{
    int no;
    int weight;
    struct Vertex* next;
}Vertex;

typedef struct 
{
    int vCount; // 정점의 개수
    Vertex* v[N]; 
}Graph;

void init(Graph* G)
{
    G->vCount = 0;
    for (int i = 0; i < N; i++)
        G->v[i] = NULL;
}

void makeVertex(Graph* G)
{
    G->vCount++;
}

void insertEdge(Graph* G, int w, int v1, int v2)
{
    Vertex* p = (Vertex*)malloc(sizeof(Vertex));
    p->weight = w;
    p->no = v1 + 1;
    p->next = G->v[v2];
    G->v[v2] = p;

    Vertex* q = (Vertex*)malloc(sizeof(Vertex));
    q->weight = w;
    q->no = v2 + 1;
    q->next = G->v[v1];
    G->v[v1] = q;
}

void print(Graph* G)
{
    for (int i = 0; i < G->vCount; i++)
    {
        Vertex* v = G->v[i];
        printf("\nV[%d] : ", i + 1);
        while (v != NULL)
        {
            printf("[%d] ", v->no);
        }
    }
}


int main()
{
    Graph G;
    init(&G);
    for (int i = 0; i < 6; i++)
        makeVertex(&G);
    print(&G);
    return 0;
}