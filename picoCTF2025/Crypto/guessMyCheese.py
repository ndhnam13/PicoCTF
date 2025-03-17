def affine_decrypt(ciphertext, a, b):
    plaintext = ""
    a_inv = pow(a, -1, 26)  # Modular inverse of a
    for char in ciphertext:
        if char.isalpha():
            # Convert to 0-25 range
            c = ord(char.upper()) - ord('A')
            # Decrypt using the inverse affine transformation
            p = (a_inv * (c - b)) % 26
            plaintext += chr(p + ord('A'))
        else:
            plaintext += char
    return plaintext

def brute_force_affine_decrypt(ciphertext):
    possible_a = [1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25]
    for a in possible_a:
        for b in range(26):
            decrypted = affine_decrypt(ciphertext, a, b)
            print(f"a={a}, b={b}: {decrypted}")


ciphertext = "QDBIJOOZEAJ" # Chesse name
brute_force_affine_decrypt(ciphertext)