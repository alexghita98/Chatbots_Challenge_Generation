#include <stdio.h>
#include <string.h>

int main() {
    char password[20];
    printf("Enter password: ");
    scanf("%19s", password);
    
    if(strcmp(password, "s3cr3t_p@ss") == 0) {
        printf("FLAG{strings_are_easy}\n");
    } else {
        printf("Access denied!\n");
    }
    
    return 0;
}