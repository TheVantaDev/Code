%{
#include <stdio.h>
extern FILE *yyin;
extern FILE *yyout;
%}

%%

"#include"<[a-z]+[.]h>        { fprintf(yyout, "%s is a header file\n", yytext); }
(int|float|char|boolean|double|float\*|char\*)   { fprintf(yyout, "%s is datatype\n", yytext); }
(main\(\)|main\(void\))       { fprintf(yyout, "%s is function\n", yytext); }
[\{\}\(\);,"]                 { fprintf(yyout, "%s is special symbol\n", yytext); }
[a-zA-Z_][a-zA-Z0-9_]*        { fprintf(yyout, "%s is identifier\n", yytext); }
(=|>|<|\+|-|/|%|>=|<=)        { fprintf(yyout, "%s is operator\n", yytext); }
(%d|%f|%s|%c)                 { fprintf(yyout, "%s is formatted output\n", yytext); }

%%

int main() {
    yyin = fopen("prog.c","r");
    if (!yyin) {
        printf("Could not open input file.\n");
        return 1;
    }
    yyout = fopen("output.txt","w");
    while(!feof(yyin)) {
        yylex();
    }
    fclose(yyin);
    fclose(yyout);
    return 0;
}

int yywrap() {
    return 1;
}