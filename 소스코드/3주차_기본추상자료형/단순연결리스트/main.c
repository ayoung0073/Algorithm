#include <stdio.h>
#include <stdlib.h>

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

void printList(LinkedListType* L)
{
    for (ListNode* p = L->head; p != NULL; p = p->link)
        printf("[%d] -> ", p->data);
    printf("NULL\n");
}

void add(LinkedListType* L, int pos, int item)
{
    ListNode* node = (ListNode*)malloc(sizeof(ListNode));
    ListNode* before = L->head;
    for (int i = 0; i < pos - 1; i++)
        before = before -> link;
    node->data = item;
    node->link = before->link;
    before->link = node;
}

void addLast(LinkedListType* L, int item)
{
    // for문에서 생각하기(add와 비슷하긴 한데)
    
}

int get(LinkedListType* L, int pos)
{
    ListNode* p = L->head;
    for(int i = 1; i < pos; i++)
        p = p->link;
    return p->data;
}

void set(LinkedListType* L, int pos, int item)
{
    ListNode* p = L->head;
    for(int i = 1; i < pos; i++)
        p = p->link;
    p->data = item;
}

// void remove()
// {
    
// }

int main()
{
    LinkedListType list;
    init(&list);
    
    addFirst(&list, 4); printList(&list);
    addFirst(&list, 10); printList(&list);
    addFirst(&list, 6); printList(&list);
    
    getchar();
    
    add(&list, 1, 40); printList(&list);
    add(&list, 3, 50); printList(&list);
    add(&list, 0, 30); printList(&list);
    
    int pos;
    printf("\n몇 번 노드의 값을 반환할까요? ");
    scanf("%d", &pos);
    printf("%d번 노드의 값은 %d\n", pos, get(&list, pos));
    return 0;
}

/*
[4] -> NULL                                                                                                                             
[10] -> [4] -> NULL                                                                                                                     
[6] -> [10] -> [4] -> NULL                                                                                                              
                                                                                                                                        
[6] -> [40] -> [10] -> [4] -> NULL                                                                                                      
[6] -> [40] -> [10] -> [50] -> [4] -> NULL                                                                                              
[6] -> [30] -> [40] -> [10] -> [50] -> [4] -> NULL                                                                                      
                                                                                                                                        
몇 번 노드의 값을 반환할까요? 2                                                                                                         
2번 노드의 값은 30                                                                                                                      
*/