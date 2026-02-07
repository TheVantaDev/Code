#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
typedef struct Node{
int val;
struct Node * parent;
struct Node *left;
struct Node *right;
bool colur;
}Node;
// 0 for black
// 1 for red
Node *root=NULL;
Node* leftrotate(Node* q) {
    Node* t = q->right;
    if (!t) return q; 
    q->right = t->left;
    if (t->left) t->left->parent = q;
    t->parent = q->parent;
    if(q->parent)
    {
        if(q==q->parent->left)
        {
            q->parent->left=t;
        }
        else {
            q->parent->right=t;
        }
    }
    else {
        root=t;
    }
    t->left = q;
    q->parent = t;
    return t;
}

Node* rightrotate(Node* q) {
    Node* t = q->left;
    if (!t) return q; 
    q->left = t->right;
    if (t->right) t->right->parent = q;
    t->parent = q->parent;
    if(q->parent)
    {
        if(q==q->parent->left)
        {
            q->parent->left=t;

        }
        else{
            q->parent->right=t;
        }
    }
    else{
        root=t;
    }
    t->right = q;
    q->parent = t;
    return t;
}
Node *insert(Node *node ,int val)
{
    if(node==NULL)
    {
        Node *p=(Node *) malloc(sizeof(Node));
        p->val=val;
        p->parent=NULL;
        p->colur=1;
        p->left=NULL;
        p->right=NULL;
      
        return p;
    }

    else if(node->val>val)
    {
       node->left= insert(node->left,val);
       node->left->parent=node;
    }
    else{
        node->right=insert(node->right,val);
        node->right->parent=node;
    }
    
  return node;
}
void fixInsert(Node *node )
{ while(node->parent && node->parent->colur==1)
    {
        Node *gp=node->parent->parent;
        if(!gp) break;
        if (node->parent == gp->left) {
            Node* uncle = gp->right;
            if (uncle && uncle->colur == 1) {
                node->parent->colur = 0;
                uncle->colur = 0;
                gp->colur = 1;
                node = gp;
            } else {
                if (node == node->parent->right) {
                    node = node->parent;
                    leftrotate(node);
                }
                node->parent->colur = 0;
                gp->colur = 1;
                rightrotate(gp);
            }
        } else {
            Node* uncle = gp->left;
            if (uncle && uncle->colur == 1) {
                node->parent->colur = 0;
                uncle->colur = 0;
                gp->colur = 1;
                node = gp;
            } else {
                if (node == node->parent->left) {
                    node = node->parent;
                    rightrotate(node);
                }
                node->parent->colur = 0;
                gp->colur = 1;
                leftrotate(gp);

                
            }

        }
    }
    root->colur=0;
}
Node* i(Node* node, int val) {
    node =insert(node, val);
    Node*cur=root;
    while(cur) {
        if (cur->val == val) break;
        else if (val < cur->val) cur = cur->left;
        else cur = cur->right;
    }
    fixInsert(cur);
    return root;
}


void display(Node *root)
{ if(root==NULL) return ;
    printf("%d",root->val);
    display(root->left);
    display(root->right);
}
int main()
{ root=i(root,10);
  root=i(root,20);
  root=i(root,5);
  display(root);
}