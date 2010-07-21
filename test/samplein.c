#include <stdio.h>
#include <stdlib.h>

int test(char **, char*);

int main(int argc, char **argv) {
    if (argc == 2) {
        printf("%s\n", ++*argv);
    }

    int i;
    for (i=0; i < 10; i++) {
        printf("%d:%d\t", i, i % 2);
    }
    printf("\n");

    /* int j;
        for (j=0; j < 50; j++) {
        printf("%d\n",j );
    }
    */

    char *a[] = {"goat", "lion", "elephant", 0};
    printf("%d\n", test(a, "animal"));

    return 0;
}

int test(char **x, char *c) {
    while (*x) {
        printf("%s: %s\n", *x, c);
        x++;
    }
}
