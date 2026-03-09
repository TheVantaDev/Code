#include <stdio.h>
#include <stdlib.h>
#include <string.h>
int state=0;
void input (char ch)
{
    switch (state)
{
case 0:
   if(ch=='\0')
      state=1;
    if(ch=='0')
      state=0;
    break;
case 1:
    if(ch=='\0')
      state=2;
    if(ch=='1')
       state=1;
    break;
case 2:
    if(ch=='\0')
      state=3;
    if(ch=='2')
       state=2;
      break;
default:
    break;
}
}
int main()
{  int n=2;
   int ch;
   printf("Enter String : ");
   for(int i=0;i<2;i++)
   { scanf("%c",&ch);
      if(ch=='0' || ch=='1' || ch=='2' || ch=='\0')
      {
        input(ch);
      }
      else{
        printf("enter only in 0 1 2\n");
      }
   }

// --qo-e->q1-e->q2
//-- self loop 0 self loop 1 self loop 2

if(state==2)
{
    printf("your string has been accepted");

}
else{
    printf("No not accepted\n");
}
    return 0;
}