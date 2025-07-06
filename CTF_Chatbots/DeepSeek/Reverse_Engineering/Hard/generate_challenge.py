import os
import subprocess

# Create original.c with proper includes
with open("original.c", "w") as f:
    f.write("""
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/ptrace.h>

void anti_debug() {
    if (ptrace(PTRACE_TRACEME, 0, 0, 0) == -1) {
        printf("Debugger detected!\\n");
        exit(1);
    }
}

void print_flag() {
    char flag[] = {0x46,0x4c,0x41,0x47,0x7b,0x70,0x34,0x63,0x6b,0x5f,0x6d,0x33,0x5f,0x75,0x70,0x7d,0x0a,0x00};
    printf("%s", flag);
}

int main() {
    anti_debug();
    char input[20];
    printf("Enter password: ");
    scanf("%19s", input);
    
    if(strcmp(input, "unpack_me_please") == 0) {
        print_flag();
    } else {
        printf("Wrong password!\\n");
    }
    return 0;
}
""")

# Compile original
print("Compiling original...")
os.system("gcc original.c -o original -no-pie -fno-stack-protector")

# Pack with UPX
print("Packing with UPX...")
os.system("upx -o packed_challenge original")

# Modify packed binary to break standard unpacking
print("Modifying packed binary...")
with open("packed_challenge", "rb") as f:
    data = bytearray(f.read())

# Change UPX magic head