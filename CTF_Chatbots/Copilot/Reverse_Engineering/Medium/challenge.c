#include <stdio.h>
#include <string.h>

char xor_key[] = {0x13, 0x37, 0x42, 0x21, 0x7F};
char target[]  = {0x75, 0x52, 0x26, 0x44, 0x1A};  // "admin" XORed with key
char flag[]    = {0x53, 0x5B, 0x4C, 0x4A, 0x5A, 0x0F, 0x1F, 0x0C, 0x1F, 0x0C, 0x1F, 0x0C, 0x1F, 0x0C, 0x1F, 0x0C, 0x00};  // XORed flag

void xor_decrypt(char *buf, int len, char *key) {
    for (int i = 0; i < len; i++) {
        buf[i] ^= key[i % 5];
    }
}

int main() {
    char input[64];
    printf("Enter password: ");
    fgets(input, sizeof(input), stdin);
    input[strcspn(input, "\n")] = 0;

    xor_decrypt(input, 5, xor_key);

    if (memcmp(input, target, 5) == 0) {
        xor_decrypt(flag, strlen((char *)flag), xor_key);
        printf("Access granted. Flag: %s\n", flag);
    } else {
        printf("Access denied.\n");
    }

    return 0;
}
