// obfuscated.c
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

// XOR decoding function
void xor_decode(unsigned char *data, int len, unsigned char key) {
    for (int i = 0; i < len; i++) {
        data[i] ^= key;
    }
}

// Red herring function
void fake_decrypt() {
    char fake[] = "FLAG{this_is_fake}";
    printf("Decoy: %s\n", fake);
}

// Another decoy
void license_check() {
    char license[] = "LICENSE_KEY_ABCD1234";
    // Unused but will appear in strings
}

int main() {
    char password[100];
    
    // XOR encoded flag with key 0x42
    unsigned char encoded_flag[] = {
        0x00, 0x2e, 0x01, 0x05, 0x5d, 0x37, 0x33, 0x36, 0x2c, 0x2b, 0x05, 
        0x1f, 0x24, 0x2a, 0x26, 0x2d, 0x37, 0x2c, 0x24, 0x2a, 0x2b, 0x5e
    };
    
    int flag_len = sizeof(encoded_flag);
    unsigned char key = 0x42;
    
    // Additional obfuscated strings
    unsigned char obf_prompt[] = {0x25, 0x2b, 0x34, 0x27, 0x36, 0x00, 0x30, 0x27, 0x37, 0x37, 0x35, 0x2d, 0x36, 0x24, 0x4a, 0x00}; // "Enter password: "
    unsigned char obf_correct[] = {0x25, 0x2d, 0x36, 0x36, 0x27, 0x25, 0x34, 0x43, 0x00}; // "Correct!"
    unsigned char obf_wrong[] = {0x35, 0x36, 0x2d, 0x2b, 0x25, 0x00, 0x30, 0x27, 0x37, 0x37, 0x35, 0x2d, 0x36, 0x24, 0x43, 0x00}; // "Wrong password!"
    
    // Decode prompt
    xor_decode(obf_prompt, strlen((char*)obf_prompt), key);
    printf("%s", (char*)obf_prompt);
    
    // Get user input
    if (fgets(password, sizeof(password), stdin) != NULL) {
        // Remove newline
        password[strcspn(password, "\n")] = 0;
        
        // Check password
        if (strcmp(password, "cybersec") == 0) {
            // Decode success message
            xor_decode(obf_correct, strlen((char*)obf_correct), key);
            printf("%s Flag: ", (char*)obf_correct);
            
            // Decode and print flag
            xor_decode(encoded_flag, flag_len, key);
            printf("%s\n", (char*)encoded_flag);
        } else {
            // Decode failure message
            xor_decode(obf_wrong, strlen((char*)obf_wrong), key);
            printf("%s\n", (char*)obf_wrong);
        }
    }
    
    return 0;
}