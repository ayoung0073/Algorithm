#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#define SWAP(x, y, t) ((t) = (x), (x) = (y), (y) = (t))
#define NUM 10
typedef struct DListNode 
{
    int elem;
    struct DListNode* prev, * next; 
}DListNode;

typedef struct 
{
    DListNode* H;
    DListNode* T; 
}SetType;

void initNode(DListNode* H, DListNode* T) 
{
    H = (DListNode*)malloc(sizeof(DListNode));
    T = (DListNode*)malloc(sizeof(DListNode));
    // H->next = (DListNode*)malloc(sizeof(DListNode));
    // H->prev = (DListNode*)malloc(sizeof(DListNode));
    // T->next = (DListNode*)malloc(sizeof(DListNode));
    // T->prev = (DListNode*)malloc(sizeof(DListNode));
    H->next = T; 
    T->prev = H;
}

void initSet(SetType* s)
{
    s->H = (DListNode*)malloc(sizeof(DListNode));
    s->T = (DListNode*)malloc(sizeof(DListNode));
    s->H->next = s->T; 
    s->T->prev = s->H;
}

void printList(SetType* s)
{
    for (DListNode* node = s->H->next; node->next != NULL; node = node->next)
    {
        printf("[%d] ", node->elem);
    }
    printf("\n");
}

void addLast(SetType* s, int item)
{
    DListNode* p = (DListNode*)malloc(sizeof(DListNode));
    p->elem = item;

    if (s->H->next == s->T) // add된 게 없을 경우
    {
        s->H->next = p;
        p->prev = s->H;
        p->next = s->T;
        s->T->prev = p;
    }
    else 
    {
        p->next = s->T->prev->next;
        p->prev = s->T->prev;
        s->T->prev->next = p;
        s->T->prev = p;
    }
}



// sort
// 제자리 선택 정렬

void selection_sort(SetType* s, int n)
{
    int least, temp;
    DListNode* save;

    for (DListNode* node = s->H->next ; node->next != NULL; node = node->next)
    {
        least = node->elem;
        save = node;
        printf("%d\n", least);
        for (DListNode* comp = node->next; comp != NULL; comp=comp->next)
        {
            // printf("%d\n", comp->elem);

            if (comp->elem < least)
            {
                save = comp;
            }
        }

        if (save != node && save != NULL)
        {
            node->prev->next = save;
            node->next->prev = save;

            save->prev->next = node;
            save->next->prev = node;
        }
    }
}

// 제자리 삽입
void insertion_sort(int list[], int n) // 배열과 배열원소 개수
{
    int i, j, save; 
    for (i = 1; i < n; i++)
    {
        save = list[i];
        for(j = i - 1; j >= 0 && list[j] > save; j--) // j 조건 범위 체크하기 !
            list[j + 1] = list[j];
        list[j + 1] = save;
    }
}

void union_set(SetType* s1, int s1_num,  SetType* s2, int s2_num)
{
    int set_[NUM];
    
}

void sub_set(SetType* s1, int s1_num,  SetType* s2, int s2_num)
{
    int set_[NUM];
    
}

int main() 
{
    SetType* s1 = (SetType*)malloc(sizeof(SetType)); 
    initSet(s1);
    SetType* s2 = (SetType*)malloc(sizeof(SetType)); 
    initSet(s2);

    srand(time(NULL));
    // addFirst(&list, 4); printList(&list);
    int n;
    printf("원소의 개수를 입력 : ");
    scanf("%d", &n);
    for (int i = 0; i < n; i++)
    {
        addLast(s1, rand() % 30 + 10);
        addLast(s2, rand() % 30 + 10);

    }

    printf("\n\n리스트 A : ");
    printList(s1);
    printf("리스트 B : ");
    printList(s2);

    selection_sort(s1 , n);
    // insertion_sort(s2, n);

    union_set(s1, NUM, s2, NUM);
    sub_set(s1, NUM, s2, NUM);
    printList(s1);

}