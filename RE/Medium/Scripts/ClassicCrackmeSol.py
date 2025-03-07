output = "mpknnphjngbhgzydttvkahppevhkmpwgdzxsykkokriepfnrdm"
secret1 = 85
secret2 = 51
secret3 = 15
fix = 97
len_out = len(output)

def decrypt(output):
    input_chars = list(output)

    for _ in range(3):  # Giải mã 3 lần ngược lại
        for i_0 in range(len_out):
            random1 = (secret1 & (i_0 % 255)) + (secret1 & ((i_0 % 255) >> 1))
            random2 = (random1 & secret2) + (secret2 & (random1 >> 2))
            input_chars[i_0] = chr(((ord(input_chars[i_0]) - fix - (random2 & secret3) - (secret3 & (random2 >> 4))) % 26) + fix)

    return "".join(input_chars)

password = decrypt(output)
print("Recovered password:", password)
