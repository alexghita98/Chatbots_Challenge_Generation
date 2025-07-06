#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int check_flag(char *input) {
    if (strlen(input) != 6) return 0;

    char x = input[0] ^ 0x21;
    char y = input[1] + 3;
    char z = input[2] - 1;

    if (x == 'F' && y == 'L' && z == 'A') {
        return strcmp(input, "FLAG42") == 0;
    }

    return 0;
}

int main() {
    char buf[64];

    // Anti-debug trick
    if (getenv("LD_PRELOAD")) {
        printf("Debugger detected!\n");
        exit(1);
    }

    printf("Enter the magic code: ");
    scanf("%s", buf);

    if (check_flag(buf)) {
        printf("Well done!\n");
        printf("flag{you_beat_the_obfuscator}\n");
    } else {
        printf("Nope.\n");
    }
}
