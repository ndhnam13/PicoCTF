Tham khảo: https://www.youtube.com/watch?v=GrUuWYwA5l0
*Sử dụng intercept rồi copy request vào repeater*

http://mercury.picoctf.net:45028/index.php

Cho 2 lựa chọn red và blue, hint nói đến việc có 1 lựa chọn thứ 3 và sử dụng burpsuite để thay đổi request

Khi sử dụng intercept trong bursuite ta thấy rằng nếu phương thức request là GET thì sẽ ra red còn POST thì là blue

GET

![image](https://github.com/user-attachments/assets/e268fcd8-1018-47fc-baa4-91111a3f1dd2)

POST

![image](https://github.com/user-attachments/assets/b565a5e5-d5c7-40bf-a2c9-7a9587f5f6e1)

Vậy nên có thể thấy rằng thay đổi request này sẽ giúp chúng ta tìm ra lựa chọn thứ 3, đó là đổi thành HEAD

![image](https://github.com/user-attachments/assets/79f7e222-b8ac-4d8d-8545-77afd4f725e3)

FLAG: picoCTF{r3j3ct_th3_du4l1ty_775f2530}
