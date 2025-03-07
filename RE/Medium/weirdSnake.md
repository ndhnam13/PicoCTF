![image](https://github.com/user-attachments/assets/1ac71344-4b8a-435a-b68b-a14e0b6ec4aa)

https://artifacts.picoctf.net/c_titan/126/snake

File `snake` là một dạng python byte code, để đưa nó về code bình thường có thể dùng chatGPT xd hoặc [pydc](https://github.com/zrax/pycdc)

Nếu dùng chatGPT thì key_str phải là `t_Jo3` chứ không phải `J_o3t`, phần tích phần dưới sẽ rõ, chắc do GPT ngu

```python
  2          84 LOAD_CONST              31 ('J')
             86 STORE_NAME               1 (key_str) # đưa J vào key_str

  3          88 LOAD_CONST              32 ('_')
             90 LOAD_NAME                1 (key_str) # + key_str nghĩa là "_J"
             92 BINARY_ADD
             94 STORE_NAME               1 (key_str)

  4          96 LOAD_NAME                1 (key_str)
             98 LOAD_CONST              33 ('o')      # key_str + o, "_Jo"
            100 BINARY_ADD
            102 STORE_NAME               1 (key_str)

  5         104 LOAD_NAME                1 (key_str)
            106 LOAD_CONST              34 ('3')      # "_Jo3"
            108 BINARY_ADD
            110 STORE_NAME               1 (key_str)

  6         112 LOAD_CONST              35 ('t')
            114 LOAD_NAME                1 (key_str)  # "t_Jo3"
            116 BINARY_ADD
            118 STORE_NAME               1 (key_str)
```

Sau đó đưa vào file weirdSnakeSol.py và chạy bằng `python3`

```python
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
```

![image](https://github.com/user-attachments/assets/0d74936c-f75e-43b2-8c5e-321ae984f36b)

`picoCTF{N0t_sO_coNfus1ng_sn@ke_7f44f566}`
