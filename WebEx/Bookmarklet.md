Khi vào trang thì sẽ có 1 đoạn code javascript


![image](https://github.com/user-attachments/assets/34fa2180-1c32-4ba9-a387-298e91d44f8c)



        javascript:(function() {
            var encryptedFlag = "àÒÆÞ¦È¬ëÙ£ÖÓÚåÛÑ¢ÕÓÓÇ¡¥Ìí";
            var key = "picoctf";
            var decryptedFlag = "";
            for (var i = 0; i < encryptedFlag.length; i++) {
                decryptedFlag += String.fromCharCode((encryptedFlag.charCodeAt(i) - key.charCodeAt(i % key.length) + 256) % 256);
            }
            alert(decryptedFlag);
        })();

Phần hint có nhắc đến việc trình duyệt web có thể chạy javascript

Trên chrome có thể dùng tổ hợp ctrl + shift + L để bật phần console, hoặc vào từ f12/console

Sau đó dán code javascript vào console rồi chạy sẽ hiện ra FLAG: picoCTF{p@g3_turn3r_0c0d211f}

![image](https://github.com/user-attachments/assets/97328d53-d2e4-40a8-b99a-a1f10e036a30)
