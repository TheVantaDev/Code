#include <stdio.h>
#define max 100
typedef struct Node
{
    int val;
    struct Node *l;
    struct Node * r;
    int h;
}Node;
Node * root = NULL;

Node * leftroate(Node * q)
{
    Node * t = q->r;
    Node * s = t->l;
    t->l = q;
    q->r = s;
    return t;
}
Node *rightrotate(Node * q){
    Node * t = q->l;
    Node *s = t->r;
    t->r=q;
    q->l=s;
    return t;
}
int maximum(Node *x ,Node *y)
{
    int a=x!=NULL ? x->h :0;
    int b=y!=NULL ? y->h:0;
    return (a>b ? a:b);
}
int balancefactor(Node *q)
{
    int a=q->left!=NULL ? q->left->h:0;
    int b=q->right!=NULL ? q->right->h:0;
    return a-b;
}
Node * delete(Node *root , int val){
 if(!root) return NULL;
 if(root->val < val){
    root = delete(root->r , val);
 }
 else if(root->val > val){
   root = delete(root->l , val);
 }
 else {
    if(!root->l || !root->r){
        Node *temp ;
        if(root->l!=NULL){
        temp = root->l;
        }
        else {
        temp = root->r;
        }
        free(root);
        return temp;
    }
    else {
        Node * succ = minValue(root->r);
        root->val = succ->val;
        root->r =delete(root->r , val);
    }
    root->h = 1+maximum(root->l->h , root->r->h);
    int bf = balancefactor(root);
    if(bf > 1 && balancefactor(root->l) >=0){
    return rightrotate(root-);
    }
    else if(bf >1 && balancefactor(root->l) <0 ){
      root-> l = leftroate(root->l);
      return rightrotate(root); 
    }
    else if(bf < -1 && balancefactor(root->r) >=0 ){
     root->r =rightrotate(root->r);
     return leftroate(root->l);
    }
    else if(bf < -1 && balancefactor(root->r) < 0 ){
     return leftroate(root);
    }
    return root;
 }
}
Node *minValue(Node * temp){
    Node * curr = temp;
    while(curr->l!=NULL){
        curr = curr->l;
    }
    return curr;
}
Node * insert(Node * ptr , int val){
    if( ptr == NULL){
        Node * p = (Node *) malloc(sizeof(Node));
        p->val=val;
        p->l=NULL;
        p->r=NULL;
        p->h=1;
        return p;
    }
    else{

        if(ptr->val < val){
            ptr->r = insert(ptr->r , val); 
        }
        else {
            ptr->l=insert(ptr->l , val);
        }
    }

    int bf = balnace(ptr);
    ptr->h = 1+maximum(ptr->r->h , ptr->l->h);
    if(bf > 1 && ptr->l->val < val){
      ptr->l = leftrotate(ptr->l);
      ptr = rightrotate(ptr);
    }
    else if(bf > 1 && ptr->l->val > val){
       ptr = rightrotate(ptr);
    }
    else if(bf < -1 && ptr->r->val < val){
      ptr = leftrotate(ptr);
    }
    else if(bf < -1 && ptr->r->val > val){
      ptr->r=rightrotate(ptr->r);
      ptr = leftrotate(ptr);
    }
    return ptr;

}

int main(){
 
    root = 
}