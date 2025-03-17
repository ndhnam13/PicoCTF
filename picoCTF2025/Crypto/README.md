# hashcrack, EVEN RSA CAN BE BROKEN???, Guess My Cheese (Part 1)
# hascrack
![image](https://github.com/user-attachments/assets/0c341684-e7d8-41f7-b019-ecd283dd8618)

- Khi kết nối đến server sẽ đưa cho ta một đoạn hash, nhiệm vụ là phải giải mã đoạn hash đó ra mật khẩu thực sự, vì các mật khẩu admin đặt rất yếu nên chắc chắn ta có thể crack được chúng

![image](https://github.com/user-attachments/assets/361365f7-95a6-4c77-b472-a3fec4c1645d)

- Có thể dùng các tool crack hash + wordlist nhưng vì có nhiều loại hash nên e đưa lên trên https://crackstation.net/ và đều crack được tất cả các hash của bài

![image](https://github.com/user-attachments/assets/ab93cb1b-2ac3-432b-8573-1f42924fd670)

`picoCTF{UseStr0nG_h@shEs_&PaSswDs!_36a1cf73}`

# EVEN RSA CAN BE BROKEN???
![image](https://github.com/user-attachments/assets/74bab26d-1c59-4213-ba4e-22dc10881114)

- Kết nối đến server ta có các đoạn mã, xem script `encrypt.py` ta biết rằng encrypt.py được sử dụng để mã hoá flag bằng thuật toán RSA rồi in ra N, e, cyphertext
- Nhiệm vụ của ta sẽ là giải mã nó

![image](https://github.com/user-attachments/assets/cac4ee97-98ac-467e-b999-f94d1193c0d0)

- Bài này e đưa lên chatgpt để viết script giải mã
``` py
from Crypto.Util.number import long_to_bytes, inverse
from sympy import factorint

# Các giá trị lấy từ output của chương trình trên
N = 25980012019461683463263868065016764698221965642002442333502779735755085274210755702286591270267918074849033508659456067429098930383720795182937256508848866  # Thay bằng N thực tế
e = 65537
ciphertext = 22342849155926666675531410873342258305516509919719368698371713373660784375489090075882648223610593221419242936363672393045657305941180849417985395234437177  # Thay bằng cypher thực tế

# Bước 1: Phân tích N thành p và q
factors = factorint(N)  # Tự động tìm p, q
p, q = list(factors.keys())

# Bước 2: Tính phi(N)
phi = (p - 1) * (q - 1)

# Bước 3: Tính d
d = inverse(e, phi)

# Bước 4: Giải mã
M = pow(ciphertext, d, N)
flag = long_to_bytes(M)

print("Flag:", flag.decode())
```
![image](https://github.com/user-attachments/assets/3e6cbb14-906b-45f0-8d91-27908570ca98)

`picoCTF{tw0_1$_pr!m33991588e}`

# Guess My Cheese (Part 1)
![image](https://github.com/user-attachments/assets/de4d7430-3ce8-4ea5-aaff-530f86594013)

- Khi kết nối đến server ta có được một đoạn text là mã hoá của một loại phô mai nào đó `QDBIJOOZEAJ` và 2 lựa chọn là đoán loại phô mai đó hoặc mã hoá 1 loại phô mai, ở đây thử mã hoá `CHEDDAR` và có `XCZYYVM`

![image](https://github.com/user-attachments/assets/fecfa65e-635d-4c3d-b735-f30fdb267743)

- Hint có nhắc đến `The one that incorporates your affinity for linear equations???`, google tìm được một kết quả khá hứa hẹn là `affine cipher` https://en.wikipedia.org/wiki/Affine_cipher

![image](https://github.com/user-attachments/assets/82098293-3a7c-489b-b199-e4531e01f43f)

- Ở đây D(x) là kí tự gốc sau giải mã, x là kí tự mã hoá, a và b là 2 số nguyên được chọn làm khoá mã hoá (0 <= a,b < m), m là kích thước bảng chữ cái (ở đây dùng tiếng anh nên m = 26)
- Hơn nữa, a còn phải là coprime của m => a chỉ có thể là [1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25]
- Từ đây e nhờ chatgpt viết script giải mã bằng cách chạy affine cipher với mọi cặp a,b
``` py
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
```

- Test với `XCZYYVM` trước vì ta biết giải mã sẽ ra `CHEDDAR`

![image](https://github.com/user-attachments/assets/8d3df14d-1cc4-449b-b402-c4ec02da0ecb)

- Biết được cặp số đúng là `a=1, b=21`
- Thử lại với `QDBIJOOZEAJ` ta biết tên nó là `VIGNOTTEJFO`

![image](https://github.com/user-attachments/assets/99b9fb22-7e2f-4fe2-8831-8909df55589d)

- Quay lại bài và chọn g rồi nhập `VIGNOTTEJFO`

![image](https://github.com/user-attachments/assets/20c79a73-6412-4094-95e9-8ed89a812896)

`picoCTF{ChEeSy6fa604f2}`
