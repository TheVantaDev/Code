#include <stdio.h>
//implement dfa for {R,I,O,T,C,A} that accepts all string having substring "CAT"
int state=0;
void input(char ch)
{  switch(state) {
        case 0:
            if(ch == 'c')
                state = 1;
            else
                state = 0;
            break; 
            
        case 1:
            if(ch == 'c')
                state = 1;
            else if(ch == 'a')
                state = 2;
            else
                state = 0;
            break;  
            
        case 2:
            if(ch == 't')
                state = 3;
            else if(ch == 'c')
                state = 1;
            else
                state = 0;
            break;  
            
        case 3:
            break;  
            
        default:
            state = 0;
            break;
    }
}

int  main()
{  int n=5;
    char ch;
 printf("enter string  :");
   
    for(int i=0;i<5;i++)
    {
        scanf("%c",&ch);
        if(ch == 'r' || ch == 'i' || ch == 'o' || 
           ch == 't' || ch == 'c' || ch == 'a') {  
            input(ch);
        } else {
            printf("Enter string only in RIOTCA\n");
            break;
        }
    }
     if(state == 3) {
            printf("\nString accepted\n");
            return 0;}
    printf("substring cat not is there");
return 0;
}