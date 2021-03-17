#include <stdio.h>
#include <stdlib.h>

#define SIZE 100

// 배열로 리스트 만들기

typedef struct // ArrayList 구조체 선언
{
    int V[SIZE]; // 배열
    int n; // 배열의 크기
}ArrayList;

void init(ArrayList* L) // ArrayList 초기화
{
    L -> n = 0;
}

void traverse(ArrayList* L) // 순회 메서드
{
    for(int i = 0; i < L -> n; i++)
        printf("[%d] ", L -> V[i]);
    printf("\n");
}

void add(ArrayList* L, int pos, int item)
{
    if(L -> n == SIZE) // 예외 처리
    {
        printf("fullListException...\n");
        exit(1);
    }
    if((pos < 0) || (pos > L -> n))
    {
        printf("invalidPosException...\n");
        exit(1);  
    }
    for (int i = L -> n - 1; i >= pos; i--)
        L -> V[i + 1] = L -> V[i];
    L -> V[pos] = item;
    L -> n++; // element 하나 추가
}

int remove_node(ArrayList* L, int pos)
{
    if(L -> n == 0) // 예외 처리
    {
        printf("emptyListException...\n");
        exit(1);
    }
    if((pos < 0) || (pos > L -> n - 1))
    {
        printf("invalidPosException...\n");
        exit(1);  
    }
    int item = L -> V[pos];
    for (int i = pos + 1; i <= L -> n - 1; i++)
        L -> V[i - 1] = L -> V[i];
    L -> n--;
    return item; // 제거된 node 반환
}

int main()
{
    ArrayList list;
    
    init(&list); // 초기

    add(&list, 0, 10); traverse(&list);
    add(&list, 0, 20); traverse(&list);
    add(&list, 1, 40); traverse(&list);
    add(&list, 0, 30); traverse(&list);
    add(&list, 3, 50); traverse(&list);
    
    getchar();
    remove_node(&list, 1); traverse(&list);
    remove_node(&list, 2); traverse(&list);
    
    return 0;
}

/*
[10]                                                                                                                                    
[20] [10]                                                                                                                               
[20] [40] [10]                                                                                                                          
[30] [20] [40] [10]                                                                                                                     
[30] [20] [40] [50] [10]                                                                                                                
                                                                                                                                        
[30] [40] [50] [10]                                                                                                                     
[30] [40] [10]  
*/