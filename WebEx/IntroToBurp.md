2 trang http://titan.picoctf.net:54443/ và http://titan.picoctf.net:54443/dashboard yêu cầu nhập thông tin

![image](https://github.com/user-attachments/assets/352b27ad-b693-4fe2-b4fd-b99b5f030af5)
![image](https://github.com/user-attachments/assets/473b9d13-58a0-4f13-842d-e58186f08f6c)

Phần đầu có thể nhập tuỳ ý

Phần 2 nhập gì cũng sai nên tập trung thay đổi request đến phần OTP 

Phần hint có nhắc đến việc sử dụng burpsuite để thay đổi request rằng server không "chịu đựng" được những cái request bị thay đổi

Dùng tính năng Proxy/intercept của burpsuite foward đến nhập otp

Nhập chữ số bất kỳ rồi submit

![image](https://github.com/user-attachments/assets/a7b5adfb-045d-4ee7-b9f5-2bd6567b95c4)

"otp = 999" nếu foward như bình thường sẽ bị invalid otp

Nên có thể chình request thành "optqwot = 999" thì sẽ ra Flag, nếu xoá toàn bộ "otp =" thì không được 

FLAG: picoCTF{#0TP_Bypvss_SuCc3$S_6bffad21}
