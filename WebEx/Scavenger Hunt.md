Xem source của trang web ta thấy part 1 của Flag

![image](https://github.com/user-attachments/assets/b94d0f1f-aef5-460d-ad4a-444488ea933c)

Part 2 của Flag được tìm thấy trong mycss.css 

![image](https://github.com/user-attachments/assets/20f6fed7-46ba-4874-b4ec-9cfe4e44ea20)

Vậy chỉ còn file myjs.js nhưng khi vào lại không thấy Flag chỉ có dòng comment /* How can I keep Google from indexing my website? */

![image](https://github.com/user-attachments/assets/fd2590e3-09ed-43ab-b3ac-a5d613cd3ed1)

Nếu sử dụng google ta biết được để google không index website của mình ta có thể sử dụng file robots.txt vậy nên ta vào http://mercury.picoctf.net:44070/robots.txt và tìm được part 3 của FLag

![image](https://github.com/user-attachments/assets/32279d57-c3f7-411f-adc1-58ad363d70a5)

Ở đây có nhắc đến "apache server" khi tìm kiếm trên google sẽ tìm ra "Tập tin .htaccess (hypertext access) là một file có ở thư mục gốc của các hostting và do apache quản lý, cấp quyền. File .htaccess có thể điều khiển, cấu hình được nhiều thứ với đa dạng các thông số, nó có thể thay đổi được các giá trị được set mặc định của apache." 

Vậy nên ta vào http://mercury.picoctf.net:44070/.htaccess và tìm được part 4 của Flag

![image](https://github.com/user-attachments/assets/b801a893-f15a-49f5-bb98-28a6fd9084ce)

Tiếp tục ở đây nhắc đến Mac và Store information thì ta biết rằng .DS_Store (Desktop services store) xuất hiện trong tất cả các thư mục của Mac và chứa các thuộc tính tuỳ chỉnh của thư mục đó

Truy cập http://mercury.picoctf.net:44070/.DS_Store và tìm được part 5 của Flag

![image](https://github.com/user-attachments/assets/882e596c-3527-4de9-8f78-b420eb0aebb1)


FLAG: picoCTF{th4ts_4_l0t_0f_pl4c3s_2_lO0k_7a46d25d}
