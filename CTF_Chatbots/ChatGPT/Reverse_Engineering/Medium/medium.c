#include <stdio.h>
#include <string.h>

int main() {
    char pass[50];
    printf("Enter password: ");
    scanf("%s", pass);

    if (strcmp(pass, "p@ssw0rd123") == 0) {
        printf("Correct!\n");
        printf("flag{logic_unlock_success}\n");
    } else {
        printf("Wrong password.\n");
    }

    return 0;
}
