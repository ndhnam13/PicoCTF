http://jupiter.challenges.picoctf.org:15796

Đề bài nói rằng đăng nhập vào web bằng tài khoản Joe nhưng không biết mật khẩu

![image](https://github.com/user-attachments/assets/0cfa25b5-7968-4a10-b754-604d31f5b184)

Dù vậy ta vẫn có thể đăng nhập vào web bằng một tài khoản và mật khẩu bất kỳ nhưng chưa thấy Flag được

![image](https://github.com/user-attachments/assets/bc7654c6-6b52-4eb4-a83d-3bb49768fbec)

Kiểm tra source không thấy có gì đặc biệt, ta có thể đi vào phần cookie của trang web để thay đổi người dùng

![image](https://github.com/user-attachments/assets/3dc3054b-d19a-482b-865d-4076c4f056ed)

Thử đổi username thành Joe, không có gì xảy ra

Đổi admin từ False thành True sẽ cho ta Flag

![image](https://github.com/user-attachments/assets/2e986312-3cce-455c-a916-740d8cd19687)

FLAG: picoCTF{th3_c0nsp1r4cy_l1v3s_6edb3f5f}
