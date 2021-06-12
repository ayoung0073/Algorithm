#include <stdio.h>
#include <stdlib.h>

// 원형연결리스트로 구현 ver3
typedef struct ListNode // 링크필드를 가리키기 위해 ListNode 이름 명시
{
    int elem;
    struct ListNode* next;
}ListNode;

// 시작점을 가리킬 헤드포인터
typedef struct
{
    ListNode* head;
}LinkedListType;

void init(LinkedListType* L)
{
    L->head = NULL;
}

LinkedListType* buildList(int n)
{
    LinkedListType* L = (LinkedListType*)malloc(sizeof(LinkedListType));
    init(L);

    ListNode* p = (ListNode*)malloc(sizeof(ListNode));
    p->elem = 1; // place index

    L->head = p;

    for (int i = 2; i < n + 1; i++)
    {
        p->next = (ListNode*)malloc(sizeof(ListNode));
        p = p->next;
        p->elem = i;
    }
    p->next = L->head; // 원형으로 만듬

    return L;
}

int runSimulation(LinkedListType* L, int n, int k)
{
    ListNode* p = L->head;
    while(p != p->next) // 노드의 개수가 1개가 될 때까지
    {
        for (int i = 1; i < k; i++)
            p = p->next;
        ListNode* remove = p->next; // 반환할 노드(삭제할)
        p->next = (p->next)->next;
        free(remove);
        p = p->next; // next round
    }

    return p->elem;
}

int candle(int n, int k)
{
    LinkedListType* L = buildList(n);
    int ret = runSimulation(L, n, k);

    return ret;
}

int main()
{
    printf("%d\n", candle(7, 3));
    printf("%d\n", candle(13, 3));
    printf("%d\n", candle(22, 5));
    return 0;
}