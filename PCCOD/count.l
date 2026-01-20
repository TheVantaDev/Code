%{
#include <stdio.h>

int wc = 0; 
int sc = 0;   
int lc = 0;   
int cc = 0;   
int wcEx=0;
%}

%option noyywrap
%%

[a-zA-Z]+   { wc++; cc+=yyleng; }      
[^ \t\n]+   {wcEx++;} 
[ \t]       { sc++; }       
[\n ]        { lc++; }       

%%

int main() {
    yyin=fopen("a.txt","r");
    while(!feof(yyin))
    {
        yylex();
    }
    printf("Word Count:%d Space Count:%d Line Count:%d Character Count:%d",wc,sc,lc,cc);
    printf("\nWord Count Except:%d",wcEx);
    return 0;
}