 #include <stdio.h>
 #include <stdlib.h>

 #define M 13

 typedef struct 
 {
     int key;
     int probeCount;
 }Bucket;

 typedef struct {
    Bucket A[M];     
 }HashType;

 void initHash(HashType* HT)
 {
     for (int i = 0; i < M; i++)
     {
         HT->A[i].key = 0; // key값은 0 이외의 값이다.
         HT->A[i].probeCount = 0; // 버킷에 저장될 element 몇번의 조사
     }
 }

 int h(int key)
 {
     return key % M;
 }

 int h2(int key)
 {
     return 11 - (key % 11); // 일반적으로 많이 사용 이중 해싱
 }

 int getNextBucketLinear(int v, int i) // 선형 조사
 {
     return (v + i) % M;
 }

int getNextBucketQuadratic(int v, int i) // 이차 조사
{
    return (v + i * i) % M;
}


int getNextBucketDouble(int v, int i, int key) // 이중 해싱
{
    return (v + i * h2(key)) % M;
}

int isEmpty(HashType* HT, int b)
{
    return HT->A[b].key == 0;
}

void insertItem(HashType* HT, int key)
{
    int v = h(key);
    int i = 0;
    int count = 0; // 시도 횟수

    while (i < M)
    {
        count++;
        int b = getNextBucketLinear(v, i);
        // int b = getNextBucketQuadratic(v, i);
        // int b = getNextBucketDouble(v, i, key);
        if (isEmpty(HT, b))
        {
            HT->A[b].key = key;
            HT->A[b].probeCount = count;
            return;
        }
        else
            i++;
    }
}

int findElement(HashType* HT, int key)
{
    int v = h(key);
    int i = 0;

    while (i < M)
    {
        int b = getNextBucketLinear(v, i);
        // int b = getNextBucketQuadratic(v, i);
        // int b = getNextBucketDouble(v, i, key);
        if (isEmpty(HT, b))
            return 0; // 찾는 key 존재하지 않는 경우
        else if (HT->A[b].key == key)
            return key;
        else
            i++;
    }
    return 0;
}

int removeElement(HashType* HT, int key)
{
    int v = h(key);
    int i = 0;

    while (i < M)
    {
        int b = getNextBucketLinear(v, i);
        // int b = getNextBucketQuadratic(v, i);
        // int b = getNextBucketDouble(v, i, key);
        if (isEmpty(HT, b)) // 지우려는 key 존재하지 않는 경우
            return 0; 
        else if (HT->A[b].key == key)
        {   
            HT->A[b].key = 0;
            HT->A[b].probeCount = 0;
            return key;
        }
        else
            i++;
    }
    return 0;
}

void printHashTable(HashType* HT)
{
    printf("Bucket  Key Probe\n");
    printf("=================\n");

    for (int i = 0; i < M; i++)
        printf("HT[%02d]: %2d   %d\n", i, HT->A[i].key, HT->A[i].probeCount);
}

int main()
{
    HashType HT;
    initHash(&HT);

    insertItem(&HT, 25);
    insertItem(&HT, 13);
    insertItem(&HT, 16);
    insertItem(&HT, 15);
    insertItem(&HT, 7);
    insertItem(&HT, 28);
    insertItem(&HT, 31);
    insertItem(&HT, 20);
    insertItem(&HT, 1);
    insertItem(&HT, 38);

    printHashTable(&HT);

    // findElement
    int key;
    printf("\n탐색할 키 입력 : ");
    scanf("%d", &key);
    if (findElement(&HT, key))
        printf("\n키 값 %d이(가) 존재합니다. \n", key);
    else
        printf("\n키 값 %d이(가) 없습니다. \n", key);


    // removeElement
    printf("\n삭제할 키 입력 : ");
    scanf("%d", &key);
    if (removeElement(&HT, key))
        printf("\n키 값 %d이(가) 삭제되었습니다. \n", key);
    else
        printf("\n키 값 %d이(가) 없습니다. \n", key); 

    printHashTable(&HT);

    return 0;
}

/* 
1. 선형조사
HT[01]:  1   1
HT[02]: 15   1
HT[03]: 16   1
HT[04]: 28   3
HT[05]: 31   1
HT[06]: 38   8
HT[07]:  7   1
HT[08]: 20   2
HT[09]:  0   0
HT[10]:  0   0
HT[11]:  0   0
HT[12]: 25   1

2. 이차조사
Bucket  Key Probe
=================
HT[00]: 13   1
HT[01]:  1   1
HT[02]: 15   1
HT[03]: 16   1
HT[04]:  0   0
HT[05]: 31   1
HT[06]: 28   3
HT[07]:  7   1
HT[08]: 20   2
HT[09]:  0   0
HT[10]:  0   0
HT[11]: 38   6
HT[12]: 25   1

3. 이중해싱
Bucket  Key Probe
=================
HT[00]: 13   1
HT[01]:  1   1
HT[02]: 15   1
HT[03]: 16   1
HT[04]: 28   4
HT[05]: 31   1
HT[06]:  0   0
HT[07]:  7   1
HT[08]:  0   0
HT[09]: 20   2
HT[10]:  0   0
HT[11]: 38   3
HT[12]: 25   1
*/