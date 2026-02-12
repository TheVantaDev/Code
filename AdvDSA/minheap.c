#include <stdio.h>
#include <stdlib.h>
#define max 100
int heap[max];
int length=0;
void swap(int *a ,int *b)
{
    int temp=*a;
    *a=*b;
    *b=temp;
}
void insert(int val)
{ 
    if(length==max)
    {
        printf("Overflow");
    }
    heap[length]=val;
    int size=length;
    length++;
    while(size>0 && heap[size]<heap[(size-1)/2] )
    { swap(&heap[size],&heap[(size-1)/2]);
        size=(size-1)/2;
    }
}
void delete(int val)
{ int index=-1;
    for(int i=0;i<length;i++)
    {
        if(heap[i]==val)
        {
            index=i;
            break;
        }
    }
    if(index==-1)
    {
        printf("Not found at all");
        return;
    }
    heap[index]=heap[length-1];
    length--;
    while(1)
    {
        int lc=2*index+1;
        int rc=2*index+2;
        int smallest=index;
        if(lc<index && heap[smallest]>heap[lc])
        {
            smallest=lc;
        }
        else if(rc<index &&heap[smallest]>heap[rc])
        {
            smallest=rc;
        }
        else if(smallest!=index)
        { swap(&heap[index],&heap[smallest]);
           index=smallest;
        }
        else 
        {break;
        }
    }

}
void display()
{
    for(int i=0;i<length;i++)
    {
        printf("%d->",heap[i]);
    }
}
int main() 
{
insert(10);
insert(20);
insert(5);
insert(6);
insert(9);
insert(11);
insert(1);
    display();
    delete(1);
    printf("\n");
   printf("after delted:"
   );
   printf("\n");
    display();
    return 0;
}