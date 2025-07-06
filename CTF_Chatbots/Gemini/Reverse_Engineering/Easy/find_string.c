#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int main() {
    // This program doesn't do much, but it hides a secret!
    char secret_message[] = "Welcome to the reverse engineering challenge!";
    char flag[] = "flag{strings_are_your_friend}"; // The actual flag

    printf("Hello, Hacker! Nothing to see here. Move along.\n");

    // Prevent compiler from optimizing out unused strings (optional but good practice for CTFs)
    volatile int dummy = 0;
    if (dummy == 1) {
        printf("%s %s\n", secret_message, flag);
    }

    return 0;
}