#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
typedef struct Node
{
    int val;
    struct Node * l;
    struct Node * r;
    bool lthread , rthread;
}Node;
Node * root = NULL;
Node *create(int val){
    Node * p = (Node *) malloc(sizeof(Node));
    p->l = NULL;
    p->r = NULL;
    p->val=val;
    p->l = 1;
    p->r=1;
    return p;
}
void insert(int val)
{  
    Node * p = create(val);
    Node *parent = root;
    if(root == NULL){
      root = p;
      return;
}
else {
    while(1){
        if(parent->val > p->val ){
            if(parent->lthread){
                p->l = parent->l;
                p->r = parent;
                parent->l = p;
                parent->lthread = 0; 
            }
            else {
                parent = parent->l;
            }
        }
        else if(parent->val < p->val){
            if(parent->rthread){
                p->r = parent->r;
                p->l = parent;
                parent->r = p;
                parent->rthread = 0;
            }
            else {
                parent = parent->r;
            }
        }
    }
}
}
Node * leftmost(Node *q){
    if(!q) return NULL;
    while(!q->lthread){
        q = q->l;
    }
    return q;
}
void inorder(Node * root){
    Node * curr = leftmost(root);
    while(curr != NULL){
        if(curr->rthread){
            curr= curr.r;
        }
        else {
            curr = leftmost(curr->r);
        }
    }
}
void preorder(Node * root){
    Node * curr = root;
    
}

int main(){

}