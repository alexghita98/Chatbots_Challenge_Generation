// mystery_binary.c
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

// Base64 decode function
int base64_decode(const char *input, char *output) {
    const char *chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/";
    int i, j = 0;
    int len = strlen(input);
    int val = 0, valb = -8;
    
    for (i = 0; i < len; i++) {
        char c = input[i];
        if (c == '=') break;
        
        char *pos = strchr(chars, c);
        if (pos == NULL) continue;
        
        val = (val << 6) | (pos - chars);
        valb += 6;
        if (valb >= 0) {
            output[j++] = (val >> valb) & 0xFF;
            valb -= 8;
        }
    }
    output[j] = '\0';
    return j;
}

// Hidden flag construction
void construct_flag(char *flag) {
    // Flag parts encoded in base64
    char part1[] = "RkxBR3ti";      // FLAG{bi
    char part2[] = "aW5hcnlf";      // nary_
    char part3[] = "YW5hbHlz";      // analys
    char part4[] = "aXNfY29t";      // is_com
    char part5[] = "cGxldGV9";      // plete}
    
    // Concatenate all parts
    char encoded[256] = {0};
    strcat(encoded, part1);
    strcat(encoded, part2);
    strcat(encoded, part3);
    strcat(encoded, part4);
    strcat(encoded, part5);
    
    // Decode the flag
    base64_decode(encoded, flag);
}

// Dummy function to make analysis more interesting
int verify_license() {
    char license[] = "DEMO_LICENSE_KEY_12345";
    printf("License: %s\n", license);
    return 1;
}

// Another dummy function with red herring
void debug_info() {
    char fake_flag[] = "FLAG{this_is_not_the_real_flag}";
    // This won't be printed, but will appear in strings
}

int main() {
    char flag[256];
    
    printf("Binary Analysis Challenge\n");
    printf("========================\n");
    
    // Call dummy functions
    if (verify_license()) {
        printf("License verified.\n");
    }
    
    // Get the real flag
    construct_flag(flag);
    
    printf("Analysis Status: Complete\n");
    printf("Result: %s\n", flag);
    
    return 0;
}