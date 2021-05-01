#include <stdio.h>
#include <stdlib.h>

typedef int element;

typedef struct ListNode {
	element data;
	ListNode* link;
}ListNode;

typedef struct ListType {
	ListNode* head;
	ListNode* tail;
}ListType;

ListType* insert_last(ListType* p, element data) {
	ListNode* new_node = (ListNode*)malloc(sizeof(ListNode));
	new_node->data = data;
	new_node->link = NULL;
	if (p->head == NULL) {
		p->head = new_node;
		p->tail = new_node;
	}
	else {
		p->tail->link = new_node;
		p->tail = new_node;
	}
	return p;
}

int findMax(ListType* p) {
	ListNode* temp = NULL;
	int max = 0;
	for (temp = p->head; temp != NULL; temp = temp->link) {
		//printf("%3d", p->data);
		if (max < temp ->data) max = temp->data;
	}
	return max;
}

int findMin(ListType* p) {
	ListNode* temp = NULL;
	int min = p->head->data;
	for (temp = p->head; temp != NULL; temp = temp->link) {
		//printf("%3d", p->data);
		if (min > temp->data) min = temp->data;
	}
	return min;
}

void print_list(ListType* p) {
	for (ListNode* node = p->head; node != NULL; node = node->link) {
		printf("%5d", node->data);
	}
	printf("\n");
}

int main() {
	int num = 0;
	ListType* p = (ListType*)malloc(sizeof(ListType));
	p->head = NULL;
	p->tail = NULL;
	while (1) {
		printf("Input an integer to add(0 to quit): ");
		scanf_s("%d", &num);
		if (num == 0) break;
		insert_last(p, num);
		print_list(p);
	}
	printf("����Ʈ �ּ�: %d\n", findMin(p));
	printf("����Ʈ �ִ�: %d\n", findMax(p));
	return 0;
}