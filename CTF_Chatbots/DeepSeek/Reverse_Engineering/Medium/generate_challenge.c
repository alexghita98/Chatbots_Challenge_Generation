#include <stdio.h>
#include <string.h>
#include <stdlib.h>

void transform(char* input) {
    for (int i = 0; i < strlen(input); i++) {
        input[i] = input[i] ^ 0x55;
    }
}

int main(int argc, char** argv) {
    if (argc != 2) {
        printf("Usage: %s <password>\n", argv[0]);
        return 1;
    }

    char buffer[32];
    strcpy(buffer, argv[1]);
    transform(buffer);

    if (strcmp(buffer, "l3t_m3_1n") == 0) {
        printf("FLAG{xor_obfuscation}\n");
    } else {
        printf("Access denied!\n");
    }

    return 0;
}