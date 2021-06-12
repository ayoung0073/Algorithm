#include <stdio.h>
#include <stdlib.h>

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
    ListNode* node = (ListNode*)malloc(sizeof(ListNode));
    node->data = item;
    node->link = L->head;
    L->head = node;
}

void printList(LinkedListType* L)
{
    // ListNode 가 아니라 ListNode* 임 pointer니까 변수 p로 하자
    for (ListNode* p = L->head; p != NULL; p = p->link)
    {
        printf("[%d] -> ", p->data);
    }
    printf("NULL\n");
}

void add(LinkedListType* L, int pos, int item)
{
    ListNode* node = (ListNode*)malloc(sizeof(ListNode));
    ListNode* p = L->head; // 이미 헤드노드로 초기화 했으니까 for문에서 pos - 1 해도 되는 듯하다.
    for (int i = 0; i < pos - 1; i++)
    {
        p = p->link;
    }
    node->data = item;
    node->link = p->link;
    p->link = node;
}

void addLast(LinkedListType* L, int item)
{
    ListNode* node = (ListNode*)malloc(sizeof(ListNode));
    ListNode* p;
    // 마지막 노드까지 이동
    for (p = L->head; p->link != NULL; p = p->link);
    node->data = item;
    node->link = NULL; // p->link와 같은 뜻?
    p->link = node;
}

int get(LinkedListType* L, int pos)
{
    ListNode* p = L->head; // 이미 헤드노드로 초기화 했으니까 for문에서 pos - 1 해도 되는 듯하다.
    for (int i = 0; i < pos - 1; i++)
    {
        p = p->link;    
    }

    return p->data;
}

void set(LinkedListType* L, int pos, int item)
{
    ListNode* p = L->head;
    for (int i = 0; i < pos - 1; i++)
    {
        p = p->link;
    }
    p->data = item;
}

int remove_node(LinkedListType* L, int pos)
{
    ListNode* before = L->head;
    // 삭제할 이전 노드를 알아야하므로 하나 덜 반복한다. 
    // 이미 헤드노드로 초기화했으므로, 덜 반복 -> pos - 2
    for (int i = 0; i < pos - 2; i++)
    {
        before = before->link;
    }
    ListNode* remove = before->link; // 삭제할 노드 저장해두기
    int remove_data = remove->data;
    before->link = remove->link;
    free(remove);
    return remove_data;
}

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

    getchar();
    
    addLast(&list, 100); printList(&list);
    addLast(&list, 200); printList(&list);
    
    getchar();

    remove_node(&list, 2); printList(&list);
    
    remove_node(&list, 2); printList(&list);

    int pos;
    printf("\n몇 번 노드의 값을 반환할까요? ");
    scanf("%d", &pos);
    printf("%d번 노드의 값은 %d\n", pos, get(&list, pos));
    return 0;
}
