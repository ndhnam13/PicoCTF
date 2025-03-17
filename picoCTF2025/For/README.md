![image](https://github.com/user-attachments/assets/273058fd-bbb7-45b6-bf45-cf3024c7ce56)# Ph4nt0m 1ntrud3r, RED, flags are stepic, Bitlocker-1, Event-Viewing

# Ph4nt0m 1ntrud3r
![image](https://github.com/user-attachments/assets/8c74139f-a64c-4528-8051-16dd2725d791)

- Bài cho ta một file pcapng, và hint có nói đến việc máy bị tấn công "in a timely manner", và cần filter packets vậy nên e đã nghĩ đến việc filter theo thời gian và xem phần data
- Xem qua bằng wireshark biết được rằng trong phần tcp.payload có chứa một đoạn được mã hoá bằng base64
- Filter các trường là  và sau đó copy phần tcp.payload và giải mã base64 rồi loại bỏ các ký không đọc được ta có flag
- Sử dụng tshark: `tshark -r myNetworkTraffic.pcap -Y "tcp.payload" -T fields -e frame.time_epoch -e tcp.payload | sort -n | awk '{print $2}' | xxd -r -p | base64 -d`
![image](https://github.com/user-attachments/assets/eb2c2305-25b4-4ce5-b2a0-878b2ad4c3a1)

`picoCTF{1t_w4snt_th4t_34sy_tbh_4r_966d0bfb}`

# RED
![image](https://github.com/user-attachments/assets/ea1c580a-7213-4257-9d23-c5620e915ad2)

![red](https://github.com/user-attachments/assets/18723072-c85b-4395-b78d-7d891c8e8d82)

- Bài cho ta một bức ảnh, ta sẽ cần tìm ra một đoạn mã bị giấu ở trong nó, hint có nói "What is facebook called rn?" - Meta, nghĩ ngay đến việc kiểm tra metadata của ảnh

![image](https://github.com/user-attachments/assets/d6431efe-6b0b-4be8-8834-256f928c305b)
- Thấy có một đoạn thơ ở mục "poem", hint thứ 2 là "Red?Ged?Bed?Aed?" Nếu để ý các chữ cái đầu ta có "RGBA" đó là color type của ảnh này, nếu để ý kỹ bài thơ và chỉ lấy chữ cái đầu của mỗi dòng ta được "CHECK LSB"
- Ta có thể kiểm tra LSB để tìm ra đoạn mã được giấu = zsteg: `zsteg lsb red.png`

![image](https://github.com/user-attachments/assets/801c61db-769b-48b4-b5fe-abaa0ac4adb3)
- Ở mục b1 là đoạn mã base64, đó chính là flag
`picoCTF{r3d_1s_th3_ult1m4t3_cur3_f0r_54dn355_}`

# flags are stepic
![image](https://github.com/user-attachments/assets/3ec4515a-a607-41eb-a5f6-30dee2732871)

- Hint có nói rằng lá cờ của một nước mà không tồn tại sẽ chứa flag, vậy ta chỉ cần tìm được nước đó sau đó tải cờ của họ về
- Vào trang web của bài này ta sẽ có một chuỗi ảnh và tên của các nước, nếu ta chuyển sang xem source của web sẽ thấy một vị trí khá nổi bật
- `        { name: "Upanzi, Republic The",img: "flags/upz.png", style:"width: 120px!important; height: 90px!important;" },`
- Tìm trên google không thấy upanzi là một quốc gia nào hết, hơn nữa còn có thêm dòng "important" khác với các hình ảnh còn lại, đây có thể là cách các hacker giao tiếp với nhau như được đề cập
- Tải file upz.png xem metadata thì thấy rằng ảnh khá to 14173x10630, còn lại không có gì bất thường, thử dùng `zsteg -a` lại lỗi có lẽ do độ lớn của ảnh
- Tìm hiểu một lúc và xem lại tên bài `flags are stepic` nếu google `stepic stegano...` sẽ ra một tool dùng để giấu dữ liệu vào ảnh tên là `stepic` tải nó về và chạy lệnh `-d`-decode trên upz.png ra một file .txt đó chính là flag
- https://github.com/1049451037/stepic
- `stepic -d -i upz.png -o abc.txt`

![image](https://github.com/user-attachments/assets/e9aada5b-83ef-4392-8647-bb6803e81aad)

`picoCTF{fl4g_h45_fl4g51d83cb1}`

# Bitlocker-1
![image](https://github.com/user-attachments/assets/55e54639-bc15-467b-8b2a-71e91fad2365)

- File tải về là `bitlocker-1.dd` là một disk image được mã hoá bởi bitlocker, những Jacky lại chỉ sử dụng một mật khẩu đơn giản cho bitlocker drive cùng với việc hint nói đến hask cracking nên ta có thể sử dụng bitlocker2john để lấy metadata của bitlocker
```
> ./bitlocker2john -i /mnt/c/Users/admin/Desktop/bitlocker-1.dd > hash.txt

Signature found at 0x3
Version: 8
Invalid version, looking for a signature with valid version...

Signature found at 0x2195000
Version: 2 (Windows 7 or later)

VMK entry found at 0x21950c4

VMK encrypted with Recovery Password found at 0x21950e6
Searching AES-CCM from 0x2195102
Trying offset 0x2195195....
VMK encrypted with AES-CCM!!

VMK entry found at 0x2195240

VMK encrypted with User Password found at 2195262
VMK encrypted with AES-CCM
> cat hash.txt
Encrypted device /mnt/c/Users/admin/Desktop/bitlocker-1.dd opened, size 100MB
Salt: 2b71884a0ef66f0b9de049a82a39d15b
RP Nonce: 00be8a46ead6da0106000000
RP MAC: a28f1a60db3e3fe4049a821c3aea5e4b
RP VMK: a1957baea68cd29488c0f3f6efcd4689e43f8ba3120a33048b2ef2c9702e298e4c260743126ec8bd29bc6d58

UP Nonce: d04d9c58eed6da010a000000
UP MAC: 68156e51e53f0a01c076a32ba2b2999a
UP VMK: fffce8530fbe5d84b4c19ac71f6c79375b87d40c2d871ed2b7b5559d71ba31b6779c6f41412fd6869442d66d


User Password hash:
$bitlocker$0$16$cb4809fe9628471a411f8380e0f668db$1048576$12$d04d9c58eed6da010a000000$60$68156e51e53f0a01c076a32ba2b2999afffce8530fbe5d84b4c19ac71f6c79375b87d40c2d871ed2b7b5559d71ba31b6779c6f41412fd6869442d66d
Hash type: User Password with MAC verification (slower solution, no false positives)
$bitlocker$1$16$cb4809fe9628471a411f8380e0f668db$1048576$12$d04d9c58eed6da010a000000$60$68156e51e53f0a01c076a32ba2b2999afffce8530fbe5d84b4c19ac71f6c79375b87d40c2d871ed2b7b5559d71ba31b6779c6f41412fd6869442d66d
Hash type: Recovery Password fast attack
$bitlocker$2$16$2b71884a0ef66f0b9de049a82a39d15b$1048576$12$00be8a46ead6da0106000000$60$a28f1a60db3e3fe4049a821c3aea5e4ba1957baea68cd29488c0f3f6efcd4689e43f8ba3120a33048b2ef2c9702e298e4c260743126ec8bd29bc6d58
Hash type: Recovery Password with MAC verification (slower solution, no false positives)
$bitlocker$3$16$2b71884a0ef66f0b9de049a82a39d15b$1048576$12$00be8a46ead6da0106000000$60$a28f1a60db3e3fe4049a821c3aea5e4ba1957baea68cd29488c0f3f6efcd4689e43f8ba3120a33048b2ef2c9702e298e4c260743126ec8bd29bc6d58
```

- Sau đó để crack được mật khẩu ta sẽ dùng hashcat mode 22100(bitlocker) kết hợp với wordlist là rockyou.txt `hashcat -m 22100 hash.txt /usr/share/wordlists/rockyou.txt --force` ta tìm ra được mật khẩu là `jacqueline`
- Sử dụng dislocker để decrypt bitlocker rồi mount và đọc file flag.txt
- Tạo 2 file trống `mkdir -p test mounted` 

`dislocker -V bitlocker-1.dd -ujacqueline -- test`

`sudo mount -o loop,ro,ntfs-3g test/dislocker-file mounted`

`sudo cat mounted/flag.txt`

`picoCTF{us3_b3tt3r_p4ssw0rd5_pl5!_3242adb1}`

# Event-Viewing
![image](https://github.com/user-attachments/assets/91cbdb6b-bef5-46fb-bfee-d500fa649990)

- Tải về là một file evtx, từ mô tả bài ta biết được flag sẽ chia làm 3 phần 1 phần sẽ ở trong phần mềm độc mà người dùng đã tải về bằng một trình tải nào đó, phần thú 2 sẽ là khi người dùng mở file đó lên(dù họ nói là nó không làm gì nhưng thực ra đã cài mã độc vào đâu đó làm cho máy tắt nguồn mỗi khi mở) và phần thứ 3 sẽ là cái mã độc làm cho máy tắt nguồn tự động nằm ở đâu
- Hint 1 nói rằng nên filter các sự kiện trên bằng ID nên ta sẽ tìm 3 ID của các event: Tải về, mở phần mềm và tắt nguồn
- Phần 1 của flag sẽ là đoạn mã base64 nằm trong ID 1033 - Application installation started. Phần mềm có tên `Totally_legit_software` khá không legit `picoCTF{Ev3nt_vi3wv3r_`

![image](https://github.com/user-attachments/assets/c640385c-3d01-49bb-aede-5b1f4b4e21ee)

- Phần 2 của flag sẽ là đoạn mã base64 nằm trong ID 4657 - Registry modification events. Nhưng trước đó ta phải kiểm tra ID 4688 - New process creation(Khi mở phần mềm) khi xem log không thấy `Totally legit software.exe` nhưng có một process khá đặc biệt là `registry`, rất có thể phần mềm độc đã tạo registry để tự động shutdown và đúng như vậy `1s_a_pr3tty_us3ful_`

![image](https://github.com/user-attachments/assets/5444c127-cca7-456e-a397-bb2057d8189f)

![image](https://github.com/user-attachments/assets/a4f378e2-c905-4e7f-9c90-b37325d34995)

- Phần 3 của flag sẽ là đoạn mã base64 nằm trong ID 1007 - Shutdown initiated by a process. `t00l_81ba3fe9}`

![image](https://github.com/user-attachments/assets/4957e0b5-5928-462e-97bd-11714702ffa7)

`picoCTF{Ev3nt_vi3wv3r_1s_a_pr3tty_us3ful_t00l_81ba3fe9}`

