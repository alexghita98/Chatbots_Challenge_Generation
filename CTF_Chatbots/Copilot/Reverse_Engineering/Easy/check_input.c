#include <stdio.h>
#include <string.h>

int main() {
    char input[64];
    printf("Enter password: ");
    fgets(input, sizeof(input), stdin);

    // Remove newline
    input[strcspn(input, "\n")] = 0;

    if (strcmp(input, "open_sesame") == 0) {
        printf("Correct! Here is your flag: flag{reverse_easy_peasy}\n");
    } else {
        printf("Wrong password.\n");
    }

    return 0;
}
