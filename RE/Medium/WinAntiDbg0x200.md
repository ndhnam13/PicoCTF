![image](https://github.com/user-attachments/assets/ac626489-faac-4339-87d0-223cc5717813)

https://artifacts.picoctf.net/c_titan/144/WinAntiDbg0x200.zip

Tương tự như bài 0x200, nhưng ở đây có đến 2 điều kiện

Thú nhất là kiểm tra giá trị của thanh ghi `edx` và sẽ nhảy đến báo lỗi chặn debugger nếu `edx` có giá trị khác 0 => Ta đổi giá trị của `edx` thành 0

![image](https://github.com/user-attachments/assets/5e7d0c9f-5b81-48a9-b8cb-c4aea576b53a)

Thú 2 là gọi hàm kiểm tra debugger và nếu thanh ghi `eax` = 0 sẽ nhảy đến flag => Đổi giá trị của `eax` = 0

![image](https://github.com/user-attachments/assets/0642c3a1-ba47-4093-bc9a-baebb8ad571a)

`picoCTF{0x200_debug_f0r_Win_c6db2768}`
