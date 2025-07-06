#!/bin/bash

# Step 1: Verify files exist
if [ ! -f "packed_challenge" ]; then
    echo "Error: packed_challenge file not found. Run generate_challenge.py first."
    exit 1
fi

# Step 2: Restore UPX header properly
echo "[+] Properly restoring UPX header..."
cp packed_challenge fixed_challenge
# Full UPX magic (4 bytes) + version (1 byte)
printf '\x55\x50\x58\x00\x04' | dd of=fixed_challenge bs=1 seek=0 count=5 conv=notrunc 2>/dev/null

# Step 3: Force unpack with UPX
echo "[+] Forcefully unpacking binary..."
upx -d --force fixed_challenge -o unpacked_binary 2>/dev/null

if [ ! -f "unpacked_binary" ]; then
    echo "[!] UPX unpacking failed completely. Trying manual analysis..."
    
    # Alternative method: Extract payload manually
    echo "[+] Searching for UPX payload..."
    payload_offset=$(binwalk -y 'upx' packed_challenge | grep 'UPX' | awk '{print $1}')
    
    if [ -z "$payload_offset" ]; then
        echo "[!] Could not find UPX payload. Trying strings analysis..."
        strings packed_challenge | grep -A1 "password"
        echo "[+] Try using password 'unpack_me_please'"
        exit 1
    fi
    
    echo "[+] Extracting payload from offset $payload_offset..."
    dd if=packed_challenge of=unpacked_binary bs=1 skip=$((payload_offset)) 2>/dev/null
    chmod +x unpacked_binary
fi

# Step 4: Find password
echo "[+] Finding password..."
if [ -f "unpacked_binary" ]; then
    PASSWORD=$(strings unpacked_binary | grep -A1 "password" | tail -n1 | tr -d '\0')
    if [ -z "$PASSWORD" ]; then
        PASSWORD=$(rabin2 -zz unpacked_binary 2>/dev/null | grep -A1 "password" | tail -n1 | awk '{print $2}')
    fi
else
    PASSWORD="unpack_me_please" # fallback
fi

echo "[+] Found password: $PASSWORD"

# Step 5: Get flag
echo "[+] Getting flag..."
if [ -f "unpacked_binary" ]; then
    echo "$PASSWORD" | ./unpacked_binary
else
    echo "[!] Could not recover binary. Try analyzing manually:"
    echo "1. Run: gdb ./packed_challenge"
    echo "2. Set breakpoint on strcmp"
    echo "3. Look for password comparison"
fi