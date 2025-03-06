![image](https://github.com/user-attachments/assets/113b806e-6b41-4842-b98e-f85b481786a8)

https://artifacts.picoctf.net/c_titan/56/WinAntiDbg0x100.zip

Bài liên quan đến debug nên cho vào IDA r thử chạy Local Windows Debugger

![image](https://github.com/user-attachments/assets/d8e930a2-962e-4a84-a65f-bc66bd5a5a8b)

Phần output trả về như vầy, nên ta phải tìm các bypass code chặn debug

Tiếp tục kiểm tra phần mềm = graph view của IDA ta thấy sau tin nhắn "lv1..." chương trình sẽ gọi hàm `IsDebuggerPresent` sau đó `test` thanh ghi `eax` rồi thực hiện câu lệnh `jz`-"Jump if zero" 

![image](https://github.com/user-attachments/assets/83dbf4f0-8030-4b22-8227-32713af35241)

Vậy sẽ có 2 trường hợp, thanh ghi `eax` có giá trị 1 hoặc 0 tiếp tục xem các nhánh điều kiện ta biết rằng nếu =1 thì sẽ hiện câu lệnh "Opps" còn =0 thì sẽ hiện ra flag

![image](https://github.com/user-attachments/assets/d16478db-e2b5-47cd-b2c2-765fb705062a)

![image](https://github.com/user-attachments/assets/8edc340e-041c-40a3-b994-01b148418228)

Khá đơn giản, vậy ta chỉ cần chuyển giá trị của thanh ghi `eax` trước khi thực hiện câu lệnh `jz`, ta có thể làm việc này bằng cách tạo một breakpoint tại câu lệnh `test` để chương trình dừng lại trước ghi thực hiện nó

![image](https://github.com/user-attachments/assets/c66f5f63-35e0-4bac-9eab-ae797ccfed0b)

Ở phần `General register` ta thấy rằng thanh ghi `eax` hiện tại đang có giá trị 1 và chắc chắn sẽ nhảy đến câu lệnh lỗi, chỉ cần đổi value thành không rồi tiếp tục chạy chương trình ta sẽ có flag

![image](https://github.com/user-attachments/assets/a6da540a-86f2-4929-80c2-3462a15a29d6)

`picoCTF{d3bug_f0r_th3_Win_0x100_a3c3a8a5}`
