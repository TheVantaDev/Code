#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
typedef struct Node
{
    /* data */
    int data;
    struct Node *left;
    struct Node *right;
    bool lthread,rthread;
}Node;
Node *root=NULL;
Node *create(int val)
{  Node *p=(Node *)malloc(sizeof(Node));
    p->data=val;
    p->left=NULL;
    p->right=NULL;
    p->lthread=true;
    p->rthread=true;
    return p;
}
void insert(int val)
{
    Node *p=create(val);
    Node *parent=root;
    if(root==NULL)
    {
        root=p;
        return ;
    }
   
    else{
        while(true)
        {
            if(parent->data > p->data)
            { 
                if(parent->lthread)
                {
                    p->left=parent->left;
                    p->right=parent;
                    parent->left=p;
                    parent->lthread=0;
                    return;
                }
                else{
                    parent=parent->left;
                }

            }
            else{
                if(parent->rthread)
                {
                    p->right=parent->right;
                    p->left=parent;
                    parent->right=p;
                    parent->rthread=0;
                    return ;
                }
                else{
                    parent=parent->right;

                }
            }
        }

    }

}

Node *leftmost(Node *n)
{
    if(n==NULL) return NULL;
    while(!n->lthread)
    {
       n=n->left;
    }
    return n;
}
void inorder(Node *root)
{ if(root==NULL) return;
    Node *curr=leftmost(root);
    while(curr!=NULL)
    { printf("%d->",curr->data);
        if(curr->rthread) 
        {
            curr=curr->right;
        }
        else{
            curr=leftmost(curr->right);
        }
        
    }

}
void preorder(Node *root)
{
    if(root==NULL)
    {
        return;
    }
    Node *curr=root;
    while(curr!=NULL)
    {
        printf("%d->",curr->data);
        if(!curr->lthread)
        {
            curr=curr->left;
        }
       else if(!curr->rthread)
        {
            curr=curr->right;
        }
        // now you completed one left so we are following that so we have to at root so until curr.rthread will travel
        // while loop ends so will reach 100 percent at root 
        else{
            while(curr!=NULL && curr->rthread)
            {
                curr=curr->right;
            }
            if(curr!=NULL)
            {
                curr=curr->right;
            }
        }

    }
}

 
int main()
{  insert(90);
    insert(10);
    insert(50);
    insert(60);
   
    // inorder(root);
    printf("preorder\n");
    preorder(root);
    printf("inorder\n");
    inorder(root);

}