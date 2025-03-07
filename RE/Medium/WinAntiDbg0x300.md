![image](https://github.com/user-attachments/assets/f395ee7c-674b-495b-b9c7-00d83496067a)

https://artifacts.picoctf.net/c_titan/123/WinAntiDbg0x300.zip

Đưa vào DiE ta biết file được nén bằng upx, vậy cần phải giải nén có thể dùng lệnh `upx -d`

![image](https://github.com/user-attachments/assets/b81cbe66-22c8-4b76-aaae-1ce9da919404)

Cho file đã giải nén vào IDA(Run as admin), xem function `_WinMain@16_0`

Chạy thử dùng debugger lần này không hiện lỗi ra phần output mà tạo một cửa sổ báo lỗi

![image](https://github.com/user-attachments/assets/b25f6835-e05c-495c-bef1-f29916ed4fa3)

Như bài 0x100, chương trình kiểm tra giá trị của `eax` và chỉ nhảy sang `loc` còn lại nếu =0

![image](https://github.com/user-attachments/assets/8385eefa-316a-4ad1-aef7-035430b96984)

Tương tự bài 1, ta đặt breakpoint và đổi giá trị của `eax` trước khi tiếp tục chạy chương trình

Đương nhiên không dễ như vậy, lần này nếu chạy chương trình sẽ crash IDA

Kiểm tra kĩ hơn các function sẽ thấy một lệnh khá đặc biệt `push offset StartAddress`, `push offset` dùng để đẩy địa chỉ của biến hoặc hằng số vào stack

![image](https://github.com/user-attachments/assets/755c6b5e-51e2-4ed5-ae32-d92a6711bb8f)

Câu lệnh này khá quen thuộc với những câu lệnh in chữ ra màn hình

![image](https://github.com/user-attachments/assets/7dd82337-94cd-4d64-b868-4367aa2cbc68)

Kiểm tra `StartAddress` sẽ nhảy đến `StartAddress_0` và ở đây ta sẽ thấy 1 cấu trúc tương tự 2 bài AntiDbg trước đó, nhưng ở đây nếu thanh ghi `eax` mà khác 0 thì sẽ tạo ra một vòng lặp vô tận đó là lí do khiến IDA crash

![image](https://github.com/user-attachments/assets/36d44078-272d-4010-b4ba-7686d2c6c86e)

Vậy chỉ cần đặt thêm một breakpoint nữa trong `StartAddress_0` chạy chương trình, chỉnh sửa dữ liệu thanh ghi sẽ ra flag

![image](https://github.com/user-attachments/assets/f535b45b-6dc5-4b98-888b-5f216c6c0563)

`picoCTF{Wind0ws_antid3bg_0x300_aba8ee97}`
