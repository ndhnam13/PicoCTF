# Extracted input_list from the disassembly
input_list = [4, 54, 41, 0, 112, 32, 25, 49, 33, 3, 0, 0, 57, 32, 108, 23, 48, 4, 9, 70, 7, 110, 36, 8, 108, 7, 49, 10, 4, 86, 43, 104, 44, 91, 7, 18, 106, 124, 89, 78]

# Key string used for decryption
key_str = "t_Jo3"
key_list = [ord(c) for c in key_str]

# Extend key_list if it's shorter than input_list
while len(key_list) < len(input_list):
    key_list.extend(key_list)
key_list = key_list[:len(input_list)]  # Trim to match length

# XOR decryption
result = [a ^ b for a, b in zip(input_list, key_list)]
password = "".join(map(chr, result))

print("Decrypted password:", password)
