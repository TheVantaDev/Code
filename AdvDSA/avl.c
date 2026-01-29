#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#define max 50
typedef struct Node{
int val;
struct Node * left;
struct Node * right;
int h;
}Node;
Node *root=NULL;
Node *STACK[max];
int top=-1;
void push (Node *q)
{
    STACK[++top]=q;
}
Node *pop()
{
    return STACK[top--];
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
Node *leftrotate(Node *q)
{ Node *t=q->right;
    Node *s=t->left;
    t->left=q;
    q->right=s;
    q->h=1+maximum(q->left,q->right);
    t->h=1+maximum(t->left,t->right);
    return t;
}
Node *rightrotate(Node *q)
{ Node * t= q->left;
    Node *s=t->right;
    t->right=q;
    q->left=s;
    q->h=1+maximum(q->left,q->right);
    t->h=1+maximum(t->left,t->right);
    return t;

}
void delete(Node *q,int val)
{ Node *parent=NULL;
    while(q!=NULL)
    { //2 chile
        if(q->val==val)
        { if(q->left!=NULL && q->right!=NULL)
            {
                Node *t=q->right;
                push(q);
                while(t->left!=NULL)
                { push(t);
                    parent=t;
                    t=t->left;
                }
                q->val=t->val;
                q=t;
            }
              if(q->left!=NULL && q->right==NULL){//left child only
                if(parent==NULL){
                    root=q->left;
                }
                else{
                    if(parent->left==q){
                        parent->left=q->left;
                    }
                    else{
                        parent->right=q->left;
                    }
                }
            }
            if(q->left==NULL && q->right!=NULL){//right child only
                if(parent==NULL){
                    root=q->right;
                }
                else{
                    if(parent->left==q){
                        parent->left=q->right;
                    }
                    else{
                        parent->right=q->right;
                    }
                }
            }
            if(q->left==NULL && q->right==NULL){//No child only
                if(parent==NULL){
                    root=NULL;
                }
                else{
                    if(parent->left==q){
                        parent->left=NULL;
                    }
                    else{
                        parent->right=NULL;
                    }
                }
            }
            free(q); // delete the node q
            while(top!=-1){
                struct Node *p = pop();
                int bf = balancefactor(p);
                p->h = 1+maximum(p->left,p->right);
                if(bf<-1 && balancefactor(p->right)<=0){
                    p=leftrotate(p);
                }
                if(bf<-1 && balancefactor(p->right)>0){
                    p->right=rightrotate(p->right);
                    p=leftrotate(p);
                }
                if(bf>1 && balancefactor(p->left)>=0){
                    p=rightrotate(p);
                }
                if(bf>1 && balancefactor(p->left)<0){
                    p->left=leftrotate(p->left);
                    p=rightrotate(p);
                }
            }
            printf("\nData deleted");
            return;
        }
        else if(q->val>val){
            push(q);
            parent=q;
            q=q->left;
        }
        else{
            push(q);
            parent=q;
            q=q->right;
        }
    }
    // now empty stack is there 
    printf("\nNot there");
    top=-1; 
    return;

        }
    
Node *create(Node *ptr ,int val)
{
    if(ptr==NULL)
    {
        Node *p=(Node*)malloc(sizeof(Node));
        p->val=val;
        p->left=NULL;
        p->right=NULL;
        p->h=1;
        return p;
    }
    else{
        if(val>ptr->val)
        {
            ptr->right=create(ptr->right,val);
        }
        else{
            ptr->left=create(ptr->left,val);
        }
    }
    ptr->h=1+maximum(ptr->left,ptr->right);
    int bf=balancefactor(ptr);
    if(bf<-1 && val >ptr->right->val)
    { ptr=leftrotate(ptr);

    }
    if(bf<-1 && val<ptr->right->val)
    { ptr->right=rightrotate(ptr->right);
      ptr=leftrotate(ptr);
    }
    if(bf>1 && val > ptr->left->val)
    { ptr->left=leftrotate(ptr->left);
        ptr=rightrotate(ptr);
    }
    if(bf>1 && val< ptr->left->val )
    {
        ptr=rightrotate(ptr);
    }
    return ptr;
}
void display(Node * root)
{
    if(root==NULL) return;
    printf("%d->",root->val);
    display(root->left);
    display(root->right);
}
int main()
{ root=create(root,10);
  root=create(root,20);
  root=create(root,30);
  display(root);

  delete(root,10);
  printf("\n");
  display(root);
    return 0;
}