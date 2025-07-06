#include <stdio.h>
#include <string.h>
#include <stdlib.h> // For atoi, exit
#include <stdbool.h> // For bool

// Simple custom hash/checksum function
unsigned int calculate_checksum(const char* input_str) {
    unsigned int checksum = 0xABCDEF01; // Initial seed
    for (size_t i = 0; i < strlen(input_str); i++) {
        checksum = (checksum + input_str[i]) * 0x1000193; // FNV-like prime
        checksum ^= (checksum >> 16); // Mix bits
    }
    return checksum;
}

// Function to validate the license key
bool validate_license(const char* key) {
    // Expected format: KEY-PART1-PART2
    // PART1: numeric, derived from string length
    // PART2: checksum of a secret string

    char secret_data[] = "super_secret_payload_for_checksum";
    unsigned int expected_checksum = calculate_checksum(secret_data); // Pre-calculated from 'secret_data'

    char key_copy[256];
    strncpy(key_copy, key, sizeof(key_copy) - 1);
    key_copy[sizeof(key_copy) - 1] = '\0'; // Ensure null termination

    char *part1_str, *part2_str;
    char *dash1, *dash2;

    dash1 = strchr(key_copy, '-');
    if (!dash1) return false;
    *dash1 = '\0'; // Null-terminate first part

    part1_str = dash1 + 1;
    dash2 = strchr(part1_str, '-');
    if (!dash2) return false;
    *dash2 = '\0'; // Null-terminate second part

    part2_str = dash2 + 1;

    // Check 1: Length-based numeric part
    int user_part1 = atoi(part1_str);
    int expected_part1 = strlen(key_copy) * 7 + 1337; // Key derivation logic

    if (user_part1 != expected_part1) {
        return false;
    }

    // Check 2: Checksum part
    unsigned int user_checksum = strtoul(part2_str, NULL, 16); // Expect hex value for checksum

    if (user_checksum != expected_checksum) {
        return false;
    }

    return true; // All checks passed
}

int main(int argc, char *argv[]) {
    char license_key[256];
    char flag[] = "flag{reversing_is_an_art}";

    if (argc < 2) {
        printf("Usage: %s <LICENSE_KEY>\n", argv[0]);
        return 1;
    }

    strncpy(license_key, argv[1], sizeof(license_key) - 1);
    license_key[sizeof(license_key) - 1] = '\0'; // Ensure null termination

    printf("Validating license key: %s\n", license_key);

    if (validate_license(license_key)) {
        printf("License valid! Here's your secret: %s\n", flag);
    } else {
        printf("Invalid license key.\n");
    }

    return 0;
}