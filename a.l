%{
#include <stdio.h>
%}

%option noyywrap

%%
"HELLO"|"Hello"|"hello"    { printf("first word is hello\n"); }
"WORLD"|"World"|"world"    { printf("second word is correct\n"); }
.|\n                       { /* ignore other characters */ }
%%

int main()
{
    yylex();
    return 0;
}
