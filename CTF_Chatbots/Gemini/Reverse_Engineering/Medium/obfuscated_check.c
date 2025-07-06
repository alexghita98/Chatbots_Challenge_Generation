#include <stdio.h>
#include <string.h>
#include <stdlib.h> // For exit()

// Function to perform a basic XOR operation
int check_password(const char* input_password) {
    // The "correct" password bytes, XORed with a key
    // This is "reverseme" XORed with 0x42
    // 'r'^0x42 = 0x61^0x42 = 0x23
    // 'e'^0x42 = 0x65^0x42 = 0x27
    // 'v'^0x42 = 0x76^0x42 = 0x34
    // 'e'^0x42 = 0x65^0x42 = 0x27
    // 'r'^0x42 = 0x72^0x42 = 0x30
    // 's'^0x42 = 0x73^0x42 = 0x31
    // 'e'^0x42 = 0x65^0x42 = 0x27
    // 'm'^0x42 = 0x6d^0x42 = 0x2f
    // 'e'^0x42 = 0x65^0x42 = 0x27
    unsigned char expected_obfuscated[] = {0x23, 0x27, 0x34, 0x27, 0x30, 0x31, 0x27, 0x2f, 0x27, 0x00}; // Null terminated

    unsigned char xor_key = 0x42; // The XOR key

    size_t input_len = strlen(input_password);
    size_t expected_len = strlen((const char*)expected_obfuscated);

    if (input_len != expected_len) {
        return 0; // Length mismatch
    }

    for (size_t i = 0; i < input_len; i++) {
        // Obfuscate the input character with the key and compare to the expected obfuscated value
        if ((input_password[i] ^ xor_key) != expected_obfuscated[i]) {
            return 0; // Mismatch
        }
    }
    return 1; // All characters match
}

int main() {
    char password_buffer[20]; // Buffer for user input
    char flag[] = "flag{xor_is_not_encryption}";

    printf("Enter the password: ");
    if (fgets(password_buffer, sizeof(password_buffer), stdin) == NULL) {
        printf("Error reading input.\n");
        return 1;
    }

    // Remove newline character if present
    password_buffer[strcspn(password_buffer, "\n")] = 0;

    if (check_password(password_buffer)) {
        printf("Access Granted! Here's your flag: %s\n", flag);
    } else {
        printf("Access Denied! Incorrect password.\n");
    }

    return 0;
}