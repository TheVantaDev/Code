#include <stdio.h>
void sort(int arr[],int n)
{ for(int i=1;i<n;i++)
    {
        int key=arr[i];
        for(int j=i-1;j>=0;j--)
        {
            if(arr[j]>key)
            {
              arr[j+1]=arr[j];
               arr[j]=key;
            }
           
        }
    }

}
int main()
{
    int arr[]={1,2,3,4,5};
    int n=5;
    sort(arr,n);
    for(int i=0;i<n;i++)
    {
        printf("%d",arr[i]);
    }
}