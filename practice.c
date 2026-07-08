#include <stdio.h>
#include <stdlib.h>
typedef struct Node
{
    int val;
    int h;
    struct Node *l, *r;
}Node;
Node * root = NULL;
Node * create(int val){
    Node * p = (Node *)malloc(sizeof(Node));
    p.val = val;
    p.l= p.r = NULL;
    p.h=1;
    return p;
}
Node *insert(Node *q , int val){
    if(!q) return create(val);
    if(q.val <  val) q.r=insert(q.r , val);
    else q.l= insert(q.l , val);
    q.h = 1+max(q.l.h , q.r.h);
    int bf = balannce(q);

}
Node *delete()
int main()
{

}
