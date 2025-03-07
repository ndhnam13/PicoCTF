![image](https://github.com/user-attachments/assets/740836a7-7c06-4fce-b4eb-a71786a2038c)

https://artifacts.picoctf.net/c_titan/104/crackme100

Chạy file `crackme100` sẽ bắt phải nhập mật khẩu, chỉ đưa sample flag nếu mật khẩu đúng

![image](https://github.com/user-attachments/assets/8414a2c1-92b5-49b4-96ab-4294db301b6c)

Đưa phần mềm vào IDA và tạo mã giả ta có 1 chương trình mã hoá 

```c
int __fastcall main(int argc, const char **argv, const char **envp)
{
  char input[64]; // [rsp+0h] [rbp-A0h] BYREF
  char output[60]; // [rsp+40h] [rbp-60h] BYREF
  int random2; // [rsp+7Ch] [rbp-24h]
  int random1; // [rsp+80h] [rbp-20h]
  char fix; // [rsp+87h] [rbp-19h]
  int secret3; // [rsp+88h] [rbp-18h]
  int secret2; // [rsp+8Ch] [rbp-14h]
  int secret1; // [rsp+90h] [rbp-10h]
  int len; // [rsp+94h] [rbp-Ch]
  int i_0; // [rsp+98h] [rbp-8h]
  int i; // [rsp+9Ch] [rbp-4h]

  strcpy(output, "mpknnphjngbhgzydttvkahppevhkmpwgdzxsykkokriepfnrdm");
  setvbuf(_bss_start, 0, 2, 0);
  printf("Enter the secret password: ");
  __isoc99_scanf("%50s", input);
  i = 0;
  len = strlen(output);
  secret1 = 85;
  secret2 = 51;
  secret3 = 15;
  fix = 97;
  while ( i <= 2 )
  {
    for ( i_0 = 0; i_0 < len; ++i_0 )
    {
      random1 = (secret1 & (i_0 % 255)) + (secret1 & ((i_0 % 255) >> 1));
      random2 = (random1 & secret2) + (secret2 & (random1 >> 2));
      input[i_0] = ((random2 & secret3) + input[i_0] - fix + (secret3 & (random2 >> 4))) % 26 + fix;
    }
    ++i;
  }

  if ( !memcmp(input, output, len) )
    printf("SUCCESS! Here is your flag: %s\n", "picoCTF{sample_flag}");
  else
    puts("FAILED!");
  return 0;
}
```

Đưa lên chatGPT tạo một script bằng python để decrypt

```python
output = "mpknnphjngbhgzydttvkahppevhkmpwgdzxsykkokriepfnrdm"
secret1 = 85
secret2 = 51
secret3 = 15
fix = 97
len_out = len(output)

def decrypt(output):
    input_chars = list(output)

    for _ in range(3):  # Giải mã 3 lần ngược lại
        for i_0 in range(len_out):
            random1 = (secret1 & (i_0 % 255)) + (secret1 & ((i_0 % 255) >> 1))
            random2 = (random1 & secret2) + (secret2 & (random1 >> 2))
            input_chars[i_0] = chr(((ord(input_chars[i_0]) - fix - (random2 & secret3) - (secret3 & (random2 >> 4))) % 26) + fix)

    return "".join(input_chars)

password = decrypt(output)
print("Recovered password:", password)
```

Chạy script đó ta có mật khẩu đúng `mmhhkjbakavyaqprqnpbuygdymyyddkratrjsbbceizsgtbcxd`, nhập vào phần mềm sẽ chạy ra sample flag

![image](https://github.com/user-attachments/assets/a6eb9900-0379-4576-8f93-5fe7ea523df8)

Nhập mật khẩu lên web

![image](https://github.com/user-attachments/assets/c80ff9e0-30f3-4717-bb3d-1b8f5bb8d82e)

`picoCTF{s0lv3_angry_symb0ls_ddcc130f}`
