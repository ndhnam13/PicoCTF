## PIE TIME, hash-only-1,2

# PIE TIME
![image](https://github.com/user-attachments/assets/709c1e7a-1366-4e33-9a6b-bd5cbcb9bf3f)

- Qua phân tích 2 file source code và binary ta biết được chương trình sẽ in ra địa chỉ của hàm main, rồi cho người dùng nhập một địa chỉ để nhảy đến
``` c
unsigned long val;
scanf("%lx", &val);
void (*foo)(void) = (void (*)())val;
foo();
```
- scanf cho nhập địa chỉ dạng hex sau đó chuyển đổi địa chỉ đó thành một con trỏ hàm
- Hàm win sẽ in ra flag, muốn biết địa chỉ dạng hex của hàm win nằm đâu dùng `nm vuln | grep win` - nm dùng để hiển thị các ký hiệu trong 1 file, có thể là hàm, biến,....
- Địa chỉ hàm main: `0x61cf0f4fa33d`, offset main: `0x133d`, offset win: `0x12a7`
- Nhưng PIE ở đây còn có nghĩa là Position Independent Executable, địa chỉ của các hàm sẽ thay đổi khi chạy nên ta không thể nhập mỗi địa chỉ của win đc
- Nếu muốn tìm địa chỉ thực sự của hàm win ta cần công thức:
```
base_address = main_address - offset_main
win_address = base_address + offset_win
```
- Áp dụng công thức trên ta có win_address = `0x61cf0f4fa2a7`
- Kết nối server và nhập vào ta có flag

![image](https://github.com/user-attachments/assets/7a643fbf-ae98-4b97-8df3-bab24cb2083f)

`picoCTF{b4s1c_p051t10n_1nd3p3nd3nc3_cb52e722}`

# hash-only-1
![image](https://github.com/user-attachments/assets/e274fcc9-637a-4dd9-81ae-7059b32e1b9e)

- File `flaghasher` sẽ chỉ cho ta biết mã hash MD5 của file /root/flag.txt chứ không thể đọc nội dung của nó

![image](https://github.com/user-attachments/assets/00e5cbc2-3701-437c-8faf-be05f4e64689)

![image](https://github.com/user-attachments/assets/44a14b8f-fc7b-4eac-af4b-afc1514c0144)

- Kiểm tra strings của `flaghasher` ta thấy `/bin/bash -c 'md5sum /root/flag.txt'`
- Chương trình chỉ gọi `md5sum` chứ không gọi toàn bộ đường dẫn của nó như trên, vì file flaghasher có đủ quyền để đọc `/root/flag.txt` nên ta có thể tạo một file md5sum giả và $PATH Hijacking để khi `flaghasher` chạy sẽ dùng file md5sum do mình tạo ra
``` sh
ctf-player@pico-chall$ export PATH=.:$PATH
ctf-player@pico-chall$ echo "/bin/cat /root/flag.txt" > md5sum
ctf-player@pico-chall$ chmod +x md5sum
ctf-player@pico-chall$ ./flaghasher
```
![image](https://github.com/user-attachments/assets/4932272a-1599-491a-a208-73f96044076b)

`picoCTF{sy5teM_b!n@riEs_4r3_5c@red_0f_yoU_bfa4a3f5}`

# hash-only-2
![image](https://github.com/user-attachments/assets/e4d9f295-171a-4208-a844-136633964e8e)

- Lần này `flaghasher` không còn nằm trong đường dẫn hiện tại khi login vào server nữa mà nằm hẳn trong `/usr/local/bin/flaghasher`

![image](https://github.com/user-attachments/assets/9cbf3f17-c594-409e-a66a-a8716982ee37)

- Lại strings file này và ta thấy flaghasher vẫn chạy như phần 1 `/bin/bash -c 'md5sum /root/flag.txt'`, nếu làm như phần 1 thì `rbash` - shell hiện tại sẽ không cho thực hiện `export PATH=.:$PATH`
- Ở đây ta có thể dùng lệnh `bash -i` tạo một interactive shell, có thể thao tác trên bash mà không bị restricted như trên `rbash`, rồi ta thực hiện như phần 1

![image](https://github.com/user-attachments/assets/04e00e7e-28c4-4c1b-8413-0ac3bc043221)

picoCTF{Co-@utH0r_Of_Sy5tem_b!n@riEs_dab7e075}
