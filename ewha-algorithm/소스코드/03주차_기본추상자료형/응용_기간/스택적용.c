#include <stdio.h>
#include <stdlib.h>

#define SIZE 6

typedef struct StackType // 스택 구현
{ 
	int data[SIZE];
	int top;
}Stack;

void initStack(Stack* s)
{
    s->top = -1;
}

int isEmpty(Stack* s)
{
   return (s->top == -1); 
}

int isFull(Stack* s)
{
    return (s->top == SIZE - 1);
}

void push(Stack* s, int data)
{
    if (isFull(s))
    {
        printf("Overflow\n");
        exit(1);
    }
    s->top++;
    s->data[s->top] = data;
}

int pop(Stack* s)
{
    if (isEmpty(s))
    {
        printf("Stack is empty\n");
        exit(1);
    }
    return s->data[s->top--];
}

void printStack(Stack* s)
{
    for (int i = 0; i <= s->top; i++)
    {
        printf("%2d ", s->data[i]);
    }
    printf("\n");
}

void spans(int X[], int S[])
{
    Stack s;
    initStack(&s);

    for (int i = 0; i < SIZE; i++)
    {

        while (!isEmpty(&s) && X[i] > X[s.top])
        {
            pop(&s);
        }

        if (!isEmpty(&s)) 
        // 비어있지 않은 경우에는 자기보다 큰 수가 있음을 의미
        {
            S[i] = i - s.data[s.top];
        }

        else
        // 비어있는 경우 자기가 최고로 큼
        {
            S[i] = i + 1; // 개수이므로 하나 더 더하는 것인가.
        }

        push(&s, i);
        // printf("===%d===\n", i);
        // printStack(&s);
    }

    while (!isEmpty(&s))
    {
        pop(&s);
    }
}


int main()
{
    int X[SIZE] = {6, 3, 4, 2, 5, 3};
    int S[SIZE] = {0};
    
    spans(X, S);
    
    for (int i = 0; i < SIZE; i++)
        printf(" [%d] ", S[i]);
    printf("\n");

    return 0;
}
/*
 [1]  [1]  [2]  [1]  [4]  [1] 
*/