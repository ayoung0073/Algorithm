#include <stdio.h>
#include <stdlib.h>

typedef struct TreeNode {
    int key;
    struct TreeNode *parent, *left, *right;
}TreeNode;

typedef struct 
{
    TreeNode* root; // 전체 이진 탐색 트리
}TreeType;

void initTree(TreeType *T)
{
    T->root = (TreeNode*)malloc(sizeof(TreeNode)); // T->root의 경우에는 parent가 계속 NULL일 것임
    T->root->parent = T->root->left = T->root->right = NULL;
}

int isExternal(TreeNode* w)
{
    return (w->left == NULL && w->right == NULL);
}

void expandExternal(TreeNode* w) // 외부노드확장
{
    TreeNode* l = (TreeNode*)malloc(sizeof(TreeNode));
    TreeNode* r = (TreeNode*)malloc(sizeof(TreeNode));

    l->left = NULL;
    l->right = NULL;
    l->parent = w;
    r->left = NULL;
    r->right = NULL;
    r->parent = w;
    w->left = l;
    w->right = r;
}

TreeNode* treeSearch(TreeNode* v, int k)
{
    if (isExternal(v))
        return v;
    if (k == v->key)
        return v;
    else if (k < v->key)
        return treeSearch(v->left, k);
    else
        return treeSearch(v->right, k);
}

int findElement(TreeType* T, int k)
{
    TreeNode* w = treeSearch(T->root, k);

    if (isExternal(w))
        return 0;
    else
        return w->key;
}

void insertItem(TreeType* T, int k)
{
    TreeNode* w = treeSearch(T->root, k);
    if (!isExternal(w)) // isInternal 대신 사용
        return;
    else
    {
         w->key = k;
         expandExternal(w);
    }
}

TreeNode* sibling(TreeNode* z)
{
    if (z->parent->left == z)
        return z->parent->right;
    else
        return z->parent->left;
}

TreeNode* reduceExternal(TreeType* T, TreeNode* z)
{
    TreeNode* w = z->parent;
    TreeNode* g = w->parent;
    TreeNode* zs = sibling(z);
    zs->parent = g;

    if (g == NULL)
    {
        T->root = zs;
    }
    else
    {
        if (w == g->left)
            g->left = zs;
        else // if w == g->right
            g->right = zs;
    }

    free(z);
    free(w);
    return zs; 
    
}

TreeNode* inOrderSucc(TreeNode* w)
{
    w = w->right;
    while (w->left != NULL)
        w = w->left;
    return w;
}

int removeElement(TreeType* T, int k)
{
    TreeNode* w = treeSearch(T->root, k);

    if (isExternal(w)) return 0;

    TreeNode *z, *y;
    z = w->left;
    if (!isExternal(z))
        z = w->right;
    if (isExternal(z)) // case 1 : 하나가 외부 노드
        reduceExternal(T, z);
    else 
    {
        z = inOrderSucc(w);
        y = z->parent; // 중위 계승자 키값만 복사. 중위 계승자 삭제하기
        w->key = y->key;
        reduceExternal(T, z);
    }
    return k;
}

void preOrder(TreeNode* root) // 전위 순회
{
    if (isExternal(root))
        return;

    printf("[%d] ", root->key);
    preOrder(root->left);
    preOrder(root->right);
}

int main()
{
    TreeType* T = (TreeType*)malloc(sizeof(TreeType));
    initTree(T);

    insertItem(T, 9);
    insertItem(T, 2);
    insertItem(T, 1);
    insertItem(T, 7);
    insertItem(T, 15);
    insertItem(T, 11);

    preOrder(T->root); printf("\n");
    getchar();

    printf("삭제할 키 입력 : ");
    int key;
    scanf("%d", &key);
    removeElement(T, key);
    preOrder(T->root); printf("\n");
}