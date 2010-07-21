leafstorm adds macros to your C file to replace lines of code with a repeating word.

Here's an example:

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

After running `leafstorm WA sample.c > out.c`:

    #define WAWAWAWAWAWAWAWAWAWAWAWAWAWAWAWAWAWAWA x++;
    #define WAWAWAWAWAWAWAWAWAWAWAWAWAWAWAWAWAWA printf("%s: %s\n", *x, c);
    #define WAWAWAWAWAWAWAWAWAWAWAWAWAWAWAWAWA while (*x) {
	#define WAWAWAWAWAWAWAWAWAWAWAWAWAWAWAWA int test(char **x, char *c) {
	#define WAWAWAWAWAWAWAWAWAWAWAWAWAWA return 0;
	#define WAWAWAWAWAWAWAWAWAWAWAWAWA printf("%d\n", test(a, "animal"));
	#define WAWAWAWAWAWAWAWAWAWAWAWA char *a[] = {"goat", "lion", "elephant", 0};
	#define WAWAWAWAWAWAWAWAWAWAWA printf("\n");
	#define WAWAWAWAWAWAWAWAWA printf("%d:%d\t", i, i % 2);
	#define WAWAWAWAWAWAWAWA for (i=0; i < 10; i++) {
	#define WAWAWAWAWAWAWA int i;
	#define WAWAWAWAWAWA }
	#define WAWAWAWAWA printf("%s\n", ++*argv);
	#define WAWAWAWA if (argc == 2) {
	#define WAWAWA int main(int argc, char **argv) {
	#define WAWA void usage();
	#define WA int test(char **, char*);
	#include <stdio.h>
    #include <stdlib.h>
    WA
    WAWA
    WAWAWA
    WAWAWAWA
    WAWAWAWAWA
    WAWAWAWAWAWA
    WAWAWAWAWAWAWA
    WAWAWAWAWAWAWAWA
    WAWAWAWAWAWAWAWAWA
    WAWAWAWAWAWA
    WAWAWAWAWAWAWAWAWAWAWA
    WAWAWAWAWAWAWAWAWAWAWAWA
    WAWAWAWAWAWAWAWAWAWAWAWAWA
    WAWAWAWAWAWAWAWAWAWAWAWAWAWA
    WAWAWAWAWAWA
    WAWAWAWAWAWAWAWAWAWAWAWAWAWAWAWA
    WAWAWAWAWAWAWAWAWAWAWAWAWAWAWAWAWA
    WAWAWAWAWAWAWAWAWAWAWAWAWAWAWAWAWAWA
    WAWAWAWAWAWAWAWAWAWAWAWAWAWAWAWAWAWAWA
    WAWAWAWAWAWA
    WAWAWAWAWAWA

Beautiful!
