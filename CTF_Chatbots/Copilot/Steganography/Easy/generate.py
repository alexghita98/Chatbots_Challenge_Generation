from PIL import Image
import numpy as np
import random

# Load and prepare image
img = Image.open("base.png").convert("RGB")
data = np.array(img)
h, w, _ = data.shape

# Message to hide
flag = "flag{lsb_reveal_success}"
bits = ''.join(f"{ord(c):08b}" for c in flag)

# Flatten all channels for easier indexing
flat = data.reshape(-1, 3)

# Use a fixed seed to shuffle pixel order (deterministic)
random.seed(42)
indices = list(range(len(flat)))
random.shuffle(indices)

# Embed bits across RGB channels
for i, bit in enumerate(bits):
    pixel_index = indices[i // 3]
    channel = i % 3  # 0 = R, 1 = G, 2 = B
    flat[pixel_index][channel] = (flat[pixel_index][channel] & 0b11111110) | int(bit)

# Reshape and save
stego = Image.fromarray(flat.reshape(h, w, 3))
stego.save("hidden.png")
