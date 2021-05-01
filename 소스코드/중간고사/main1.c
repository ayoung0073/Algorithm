#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define NUM 10

// 단순 연결 리스트 구현
typedef struct ListNode
{
    int data; // 데이터 필드
    struct ListNode* link; // 링크 필드
}ListNode;

// 시작점을 가리킬 헤드포인터
typedef struct
{
    ListNode* head;
}LinkedListType;

void init(LinkedListType* L)
{
    L -> head = NULL;
}

void addFirst(LinkedListType* L, int item)
{
    ListNode* node = (ListNode*)malloc(sizeof(ListNode)); // 노드 생성
    node->data = item;
    node->link = L->head;
    L->head = node;
}


void addLast(LinkedListType* L, int item)
{

    ListNode* node = (ListNode*)malloc(sizeof(ListNode));
    ListNode* last;
    if (L->head == NULL)
    {
        last->data = item;
        last->link = L->head;
        L->head = last;
    }
    else
    {
        for(last = L->head; last->link != NULL; last = last->link)
        node->data = item;
        node->link = last->link;
        last->link = node;
    }
}

void printList(LinkedListType* L)
{
    for (ListNode* p = L->head; p != NULL; p = p->link)
        printf("[%d] -> ", p->data);
    printf("NULL\n");
}



int main()
{
    int n = 5;
    LinkedListType list;
    init(&list);
    srand(time(NULL));

    // addFirst(&list, 4); printList(&list);

    printf("원소의 개수를 입력하세요 : ");
    scanf("%d", &n);
    printf("%d\n", n);
    for (int i = 0; i < n; i++)
    {

        addLast(&list, rand() % 100 + 10);
    }

    printList(&list);

    return 0;


}