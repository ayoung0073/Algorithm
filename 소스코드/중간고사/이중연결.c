#include <stdio.h>

void intro();

typedef struct dListNode {
	int data; 
	struct dListNode* llink; // left link
	struct dListNode* rlink; // right link
}dListNode; 

void print_dList(dListNode* head) {
	dListNode* p = NULL;
	printf("<LIST>\n");
	for (p = head->rlink; p != head; p = p->rlink) {
		printf("%4d", p->data);
	}
	printf("\n");
}

void insert(dListNode* head, const int num) { // ��� �߰� �Լ�
	dListNode* p = (dListNode*)malloc(sizeof(dListNode)); // �߰��� �� ��� ����
	p->data = num; // �� ����
	head->rlink->llink = p; // ���� head�� ������ ����� llink�� �� ��� ����Ű�� ��
	p->rlink = head->rlink;  
	head->rlink = p; // ���� head����� rlink�� �� ��带 ����Ű�� ��
}

void ddelete(dListNode* head, int num) { // ��� ���� �Լ�
	int check = 1; // num�� �ִ��� ������ üũ�غ��� ���� ����
	
	dListNode* p = NULL;

	for (p = head->rlink; p != head; p = p->rlink) 
	{
		if (p->data == num) 
		{
			check = 0; // ������ ���� ������ ��Ÿ��
			p->llink->rlink = p->rlink; 
			p->rlink->llink = p->llink; 
			free(p); //p��ȯ
			printf("%d is found and deleted", num);
			break;
		}
	}

	if (check == 1) { // for���� �� ���� ������ ���� search������ ������
		printf("%d is not in the list", num);
	}

	printf("\n");
}


int main() { // ���� �Լ�
	intro();

	dListNode* head = (dListNode*)malloc(sizeof(dListNode));

	head->rlink = head; //���Ḯ��Ʈ �ʱ�ȭ // �����
	head->llink = head;

	int num;

	while (1) {
		printf("Input an integer to add<0 to quit>: ");
		scanf_s("%d", &num); // ���� �Է¹ޱ�

		if (num == 0) break; // 0�̸� while�� ��������
		insert(head, num);
	}

	print_dList(head); // �������߿��Ḯ��Ʈ ���

	printf("Input a number to search and delete: ");
	scanf_s("%d", &num);

	ddelete(head, num); // delete �Լ� ȣ��
	print_dList(head);

	return 0;
}


void intro() { //�а�,�й�,���� ��� �޼���
	printf("====================\n");
	printf("�а�: ���̹������а�\n");
	printf("�й�: 1971068\n");
	printf("����: ���ƿ�\n");
	printf("====================\n");
}