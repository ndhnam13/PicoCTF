![image](https://github.com/user-attachments/assets/d4d15177-18e3-4ecf-93f1-873d29925a9e)

https://artifacts.picoctf.net/c_titan/100/out

Đưa file `out` vào DiE ta biết nó là file .ELF được nén bằng upx

![image](https://github.com/user-attachments/assets/cd656a37-7836-4ee4-b445-cba5cd090dd3)

Giải nén = `upx -d` đưa lại vào DiE đây là 1 file được viết bằng ngôn ngữ C

![image](https://github.com/user-attachments/assets/938d0c8a-2080-4204-81b6-d39fc71a5336)

Chạy thử file này sẽ yêu cầu nhập mật khẩu, nếu không đúng sẽ trả `Access Denied`

![image](https://github.com/user-attachments/assets/8ce9ecfe-62c4-4098-b735-c45a2b9a043e)

Đưa vào IDA ta sẽ thấy flag là một đoạn mã hex, decode nó và ta có flag

![image](https://github.com/user-attachments/assets/21c408e3-9795-49ed-8c53-f068bf180959)

![image](https://github.com/user-attachments/assets/31401cf6-93fc-4b66-a6c7-c3fe109ac4b5)

`7069636f4354467b5539585f556e5034636b314e365f42316e34526933535f31613561336633397d`
`picoCTF{U9X_UnP4ck1N6_B1n4Ri3S_1a5a3f39}`
