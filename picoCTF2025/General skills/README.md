![image](https://github.com/user-attachments/assets/321abb01-d490-4671-8008-13a5a6f23fc4)## FANTASY CTF, Rust fixme 1,2,3

# FANTASY CTF
![image](https://github.com/user-attachments/assets/b5be2e54-faf1-4aab-918c-ff23817c37b7)

- Bài này chỉ giới thiệu về luật

`picoCTF{m1113n1um_3d1710n_fc649bc5}`

# Rust fixme 1
![image](https://github.com/user-attachments/assets/762ccadd-5513-4558-a69d-adb0ebdcb91d)

- Bài muốn ta sửa các syntax error ở trong code rust
- Thử chạy = `cargo run` ta có 3 lỗi

![image](https://github.com/user-attachments/assets/bdf0d0bf-ea3b-4395-97e9-934d38609d1a)

- Để end statement phải có dấu `;`, để format string ta dùng `"{}"` thay vì `":?"`và để return ta dùng `return` thay vì `ret`
- Sửa lại đoạn code và chạy lại ta có flag

![image](https://github.com/user-attachments/assets/a89a9418-6f5c-4909-bfaf-9d1c7c6cd86c)

# Rust fixme 2
![image](https://github.com/user-attachments/assets/1cfb9026-fcb8-4b35-bd15-6e0a5a535f8b)

- Bây giờ bài muốn ta sửa các lỗi liên quan tới borrowing https://doc.rust-lang.org/book/ch04-02-references-and-borrowing.html
- Chạy thử báo 2 lỗi

![image](https://github.com/user-attachments/assets/16d314c5-1f56-43a0-97e3-5d12a07c5992)

- Như phần complier error đã nói các tham số `borrowed_string` và `party_foul` cần phải là một mutable reference nếu muốn thay đổi nội dung của chúng
- Vậy trước các tham số này cần có thêm `&mut String` `&mut party_foul`, sửa các lỗi này và chạy sẽ in ra flag

![image](https://github.com/user-attachments/assets/c2146607-3859-4897-9bf2-98b3c4872e54)

`picoCTF{4r3_y0u_h4v1n5_fun_y31?}`

# Rust fixme 3
![image](https://github.com/user-attachments/assets/a79f3c08-ee43-48ee-b5d7-39d72964b6be)

- Tiếp tục là sửa syntax error, chạy thử trước đã, ở đây có một lỗi là `call to unsafe function` 

![image](https://github.com/user-attachments/assets/99576852-db9a-4177-b1cf-ac1b35c0d8e3)

- Đi vào trực tiếp file main.rs ta sẽ thấy thêm comment hướng dẫn

![image](https://github.com/user-attachments/assets/29ba2805-1e04-45e8-affb-24103f0cb7ce)

- decrypted_buffer ở đây có thể được sử dụng trực tiếp luôn, không cần phải tạo pointer cho nó nên ta có thể xoá luôn 3 dòng đó đi, ở dòng `push_str` thay `decrypted_slice` = `&decrypted_buffer` luôn và chạy

![image](https://github.com/user-attachments/assets/10d4c6d4-a187-44a2-97b4-2ab8e18530ae)

`picoCTF{n0w_y0uv3_f1x3d_1h3m_411}`

