// AVL 트리 응용
#include <stdio.h>
#include <stdlib.h>

#define max(a,b) (((a) > (b)) ? (a) : (b))

typedef struct TreeNode {
    int key, height;
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
    T->root->height = 0; 
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

int heightUpdateAndBalanceCheck(TreeNode* w) // 높이 균형 속성을 업데이트 하면서 균형 체크 // true, false 반환
{
    TreeNode* l, * r;
    int b;

    if (w == NULL)
        return 1;
    
    l = w->left;
    r = w->right;

    w->height = max(r->height, l->height) + 1; // 높이 균형 속성 업데이트

    b = r->height - l->height;

    if (b*b < 2) // dmatndlf tneh dlTdmsl
        return 1;
    else   
        return 0;


}

TreeNode* restructure(TreeType* T, TreeNode* x)
{
    TreeNode* y, * z, * a, * b, * c,* T0, * T1, * T2, * T3;

    y = x->parent;
    z = y->parent;

    // 단일 회전
    if (z->key < y->key && y->key < x->key) // RR
    {
        a = z;
        b = y;
        c = x;
        T0 = a->left;
        T1 = b->left;
        T2 = c->left;
        T3 = c->right;
    }
    else if (x->key < y->key && y->key < z->key) // LL
    {
        a = x;
        b = y;
        c = z;
        T0 = a->left;
        T1 = a->right;
        T2 = b->right;
        T3 = c->right;
    }

    // 이중 회전
    else if (z->key < x->key && x->key < y->key) // RL
    {
        a = z;
        b = x;
        c = y;
        T0 = a->left;
        T1 = b->left;
        T2 = b->right;
        T3 = c->right;
    }
    else // LR
    {
        a = y;
        b = x;
        c = z;
        T0 = a->left;
        T1 = b->left;
        T2 = b->right;
        T3 = c->right;
    }

    // 3.z를 루트로 하는 부트리를 b를 루트로 하는 부트리로 대체
    if (z == T->root) 
    {
        T->root = b; // T의 루트가 b를 가리키게끔
        b->parent = NULL;
    }
    else if(z->parent->left == z)
    {
        z->parent->left = b;
        b->parent = z->parent; 
    }
    else
    {
        z->parent->right = b;
        b->parent = z->parent;
    }

    // 4.
    a->left = T0;
    T0->parent = a;
    a->right = T1;
    T1->parent = a;
    a->height = max(T0->height, T1->height) + 1;

    // 5.
    c->left = T2;
    T2->parent = c;
    c->right = T3;
    T3->parent = c;
    c->height = max(T2->height, T3->height) + 1;

    // 6.
    b->left = a;
    a->parent = b;
    b->right = c;
    c->parent = b;
    b->height = max(a->height, c->height) + 1;

    return b; // root 반환
}

void searchAndFixAfterInsertion(TreeType* T, TreeNode* w)  // 삽입 후 고치기 (AVL 트리로)
{
    // w에서 T의 루트로 향해 올라가다가 처음 만나는 불균형 노드를 z라고 하자 (없다면 exit)
    TreeNode* z = w;
    TreeNode* y, * x;

    while (!heightUpdateAndBalanceCheck(z)) // 루트를 향해 올라가면서 불균형을 찾자. // false인 경우다 주의..
    {
        // 1. -----------
        if (z == NULL)
            return;
        z = z->parent;

        // z의 높은 자식 y
        // 2. -----------
        if (z->left->height > z->right->height)
            y = z->left;
        else   
            y = z->right;

        // y의 높은 자식 x
        // 3. -----------
        if (y->left->height > y->right->height)
            x = y->left;
        else if (y->left->height < y->right->height)
            x = y->right;

        // 여기까지 x, y, z 다 만들어짐 이제 restructure

        // 4. --------
        restructure(T, x);  
    }
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
         searchAndFixAfterInsertion(T, w);
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

void rFindAllnRange(TreeNode* v, int k1, int k2)
{
    if(isExternal(v))
        return;
    if (k1 <= v->key && v->key < k2)
        printf("[%d] ", v->key);
    
    if (v->key <= k1) // else if 는 안됨 주의 
        rFindAllnRange(v->right, k1, k2);
    else if (k2 <= v->key)
        rFindAllnRange(v->left, k1, k2);
    else
    {
        rFindAllnRange(v->left, k1, k2);
        rFindAllnRange(v->right, k1, k2);
    }
}

int main()
{
    TreeType* T = (TreeType*)malloc(sizeof(TreeType));
    initTree(T);

    insertItem(T, 44);
    insertItem(T, 17);
    insertItem(T, 42);
    insertItem(T, 78);
    insertItem(T, 50);
    insertItem(T, 88);
    insertItem(T, 48);
    insertItem(T, 62);
    insertItem(T, 54);
    preOrder(T->root); printf("\n");

    rFindAllnRange(T->root, 50, 80);

}