%{
#include <stdio.h>
int count = 0;   // global token counter
%}

%%
[0-9]+        { count++; fprintf(yyout, "NUMBER(%s)\n", yytext); }
[a-zA-Z]+     { count++; fprintf(yyout, "IDENTIFIER(%s)\n", yytext); }
[ \t\n]+      { /* ignore whitespace */ }
.             { count++; fprintf(yyout, "SYMBOL(%s)\n", yytext); }
%%

int yywrap() {
    return 1;  // signals end of input
}