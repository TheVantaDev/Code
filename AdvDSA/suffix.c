#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <string.h>
typedef struct Node
{ struct Node * chlild[26];
    bool eow;

}Node;
Node * root=NULL;
Node * create()
{  Node *p=(Node *)malloc(sizeof(Node));
    for(int i=0;i<26;i++)
    {  p->chlild[i]=NULL;
 
    }
    p->eow=false;
    return p;

}
void suffix(char word[])
{
    Node * p=root;
    for(int i=0;word[i]!=0;i++)
    {
        int idx=word[i]-'a';
        if(p->chlild[idx]==NULL)
        {
            p->chlild[idx]=create();
        }
        p=p->chlild[idx];
    }
    p->eow=1;
}
int insert(char word[])
{
    int n=strlen(word);
    for(int i=0;i<n;i++)
    {
        suffix(word+i);
    }
    return n;
}


void  display(Node *q,int length,int level,int f)
{   
    for(int i=0;i<26;i++)
    {
        if(q->chlild[i]!=NULL)
        {
            for(int j=0;j<level;j++)
            {
                printf("_");
            }
            printf("%c",i+'a');
           
            if(q->chlild[i]->eow )
            {
                printf("->%d",length-f-1);
                
            }
            printf("\n");
            display(q->chlild[i],length,level+1,f+1);
        }
    }


}
int main()
{ root=create();
    int a=insert("banana");
    int f=0;
    display(root,a,0,f);
    return 0;
}