#include <stdio.h>
#include <stdint.h>

#define FLAG "flag{custom_vm_cracked}"

uint8_t bytecode[] = {
    0x01, 'f',  // print 'f'
    0x01, 'l',  // print 'l'
    0x01, 'a',  // print 'a'
    0x01, 'g',  // print 'g'
    0x01, '{',
    0x01, 'c',
    0x01, 'u',
    0x01, 's',
    0x01, 't',
    0x01, 'o',
    0x01, 'm',
    0x01, '_',
    0x01, 'v',
    0x01, 'm',
    0x01, '_',
    0x01, 'c',
    0x01, 'r',
    0x01, 'a',
    0x01, 'c',
    0x01, 'k',
    0x01, 'e',
    0x01, 'd',
    0x01, '}',
    0xFF        // HALT
};

void run_vm(uint8_t *code) {
    int pc = 0;
    while (1) {
        uint8_t instr = code[pc++];
        switch (instr) {
            case 0x01:  // PRINT
                putchar(code[pc++]);
                break;
            case 0xFF:  // HALT
                return;
            default:
                printf("Unknown instruction: 0x%02x\n", instr);
                return;
        }
    }
}

int main() {
    printf("Running VM...\n");
    run_vm(bytecode);
    printf("\nDone.\n");
    return 0;
}
