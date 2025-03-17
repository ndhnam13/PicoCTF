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