#include <stdio.h>

extern FILE *yyin, *yyout;
extern int yylex();
extern int count; // updated by lexer rules

int main(int argc, char *argv[]) {
    yyin = fopen("input.txt", "r");
    if (!yyin) {
        perror("Failed to open input.txt");
        return 1;
    }

    yyout = fopen("output1.txt", "w");
    if (!yyout) {
        perror("Failed to open output1.txt");
        fclose(yyin);
        return 1;
    }

    while (yylex() != 0) {
    }

    fprintf(yyout, "Total tokens: %d\n", count);

    fclose(yyin);
    fclose(yyout);

    return 0;
}