#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
typedef struct Node
{ struct Node * child[26];
  bool eow;
}Node;
Node *root=NULL;
Node *create()
{ Node *p=(Node *)malloc(sizeof(Node));
    for(int i=0;i<26;i++)
    {  p->child[i]=NULL;
    }
    p->eow=false;
    return p;
}
void insert(char word[])
{ Node *p=root;
    for(int i=0;word[i]!='\0';i++)
    {
        int index=word[i]-'a';
        if(p->child[index]==NULL)
        {
            p->child[index]=create();
        }
        p=p->child[index];
    }
    p->eow=1;
}
void display(Node *q,int level)
{
    for(int i=0;i<26;i++)
    {
        if(q->child[i]!=NULL)
        {
            for(int j=0;j<level;j++)
            {
                printf("_");
            }
            printf("%c",i+'a');
            if(q->child[i]->eow)
            {
                printf("*");
            }
            printf("\n");
            display(q->child[i],level+1);
        }
    }
}

int main()
{ root=create();
  insert("cat");
 insert("cow");
 insert("car");
 insert("ant");
 insert("an");
 insert("a");
 display(root,0);
    return 0;
}