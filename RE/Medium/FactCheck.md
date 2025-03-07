![image](https://github.com/user-attachments/assets/1d35fec9-267b-4f23-906d-6375567836a8)

https://artifacts.picoctf.net/c_titan/191/bin

Đưa vào DiE ta biết rằng đây là một file được viết bằng C/C++

Kiểm tra trong string ta được phần đầu của flag `picoCTF{wELF_d0N3_mate_`

Muốn biết phần sau được tạo ra như nào, đưa vào IDA, và có thể để IDA tạo mã giả để xem

```cpp
int __fastcall main(int argc, const char **argv, const char **envp)
{
  __int64 v3; // rdx
  __int64 v4; // rdx
  __int64 v5; // rdx
  __int64 v6; // rdx
  __int64 v7; // rdx
  __int64 v8; // rdx
  __int64 v9; // rdx
  __int64 v10; // rdx
  __int64 v11; // rdx
  __int64 v12; // rdx
  __int64 v13; // rdx
  __int64 v14; // rdx
  __int64 v15; // rdx
  __int64 v16; // rdx
  __int64 v17; // rdx
  __int64 v18; // rdx
  int v19; // ebx
  char v21; // [rsp+Fh] [rbp-241h] BYREF
  _BYTE v22[32]; // [rsp+10h] [rbp-240h] BYREF
  _BYTE v23[32]; // [rsp+30h] [rbp-220h] BYREF
  _BYTE v24[32]; // [rsp+50h] [rbp-200h] BYREF
  _BYTE v25[32]; // [rsp+70h] [rbp-1E0h] BYREF
  _BYTE v26[32]; // [rsp+90h] [rbp-1C0h] BYREF
  _BYTE v27[32]; // [rsp+B0h] [rbp-1A0h] BYREF
  _BYTE v28[32]; // [rsp+D0h] [rbp-180h] BYREF
  _BYTE v29[32]; // [rsp+F0h] [rbp-160h] BYREF
  _BYTE v30[32]; // [rsp+110h] [rbp-140h] BYREF
  _BYTE v31[32]; // [rsp+130h] [rbp-120h] BYREF
  _BYTE v32[32]; // [rsp+150h] [rbp-100h] BYREF
  _BYTE v33[32]; // [rsp+170h] [rbp-E0h] BYREF
  _BYTE v34[32]; // [rsp+190h] [rbp-C0h] BYREF
  _BYTE v35[32]; // [rsp+1B0h] [rbp-A0h] BYREF
  _BYTE v36[32]; // [rsp+1D0h] [rbp-80h] BYREF
  _BYTE v37[32]; // [rsp+1F0h] [rbp-60h] BYREF
  _BYTE v38[40]; // [rsp+210h] [rbp-40h] BYREF
  unsigned __int64 v39; // [rsp+238h] [rbp-18h]

  v39 = __readfsqword(0x28u);
  std::allocator<char>::allocator(&v21, argv, envp);
  std::string::basic_string(v22, "picoCTF{wELF_d0N3_mate_", &v21);
  std::allocator<char>::~allocator(&v21);
  std::allocator<char>::allocator(&v21, "picoCTF{wELF_d0N3_mate_", v3);
  std::string::basic_string(v23, "5", &v21);
  std::allocator<char>::~allocator(&v21);
  std::allocator<char>::allocator(&v21, "5", v4);
  std::string::basic_string(v24, "5", &v21);
  std::allocator<char>::~allocator(&v21);
  std::allocator<char>::allocator(&v21, "5", v5);
  std::string::basic_string(v25, "7", &v21);
  std::allocator<char>::~allocator(&v21);
  std::allocator<char>::allocator(&v21, "7", v6);
  std::string::basic_string(v26, "3", &v21);
  std::allocator<char>::~allocator(&v21);
  std::allocator<char>::allocator(&v21, "3", v7);
  std::string::basic_string(v27, "0", &v21);
  std::allocator<char>::~allocator(&v21);
  std::allocator<char>::allocator(&v21, "0", v8);
  std::string::basic_string(v28, "5", &v21);
  std::allocator<char>::~allocator(&v21);
  std::allocator<char>::allocator(&v21, "5", v9);
  std::string::basic_string(v29, "a", &v21);
  std::allocator<char>::~allocator(&v21);
  std::allocator<char>::allocator(&v21, "a", v10);
  std::string::basic_string(v30, "e", &v21);
  std::allocator<char>::~allocator(&v21);
  std::allocator<char>::allocator(&v21, "e", v11);
  std::string::basic_string(v31, "f", &v21);
  std::allocator<char>::~allocator(&v21);
  std::allocator<char>::allocator(&v21, "f", v12);
  std::string::basic_string(v32, "d", &v21);
  std::allocator<char>::~allocator(&v21);
  std::allocator<char>::allocator(&v21, "d", v13);
  std::string::basic_string(v33, "b", &v21);
  std::allocator<char>::~allocator(&v21);
  std::allocator<char>::allocator(&v21, "b", v14);
  std::string::basic_string(v34, "9", &v21);
  std::allocator<char>::~allocator(&v21);
  std::allocator<char>::allocator(&v21, "9", v15);
  std::string::basic_string(v35, "6", &v21);
  std::allocator<char>::~allocator(&v21);
  std::allocator<char>::allocator(&v21, "6", v16);
  std::string::basic_string(v36, "d", &v21);
  std::allocator<char>::~allocator(&v21);
  std::allocator<char>::allocator(&v21, "d", v17);
  std::string::basic_string(v37, "7", &v21);
  std::allocator<char>::~allocator(&v21);
  std::allocator<char>::allocator(&v21, "7", v18);
  std::string::basic_string(v38, "8", &v21);
  std::allocator<char>::~allocator(&v21);
  if ( *(char *)std::string::operator[](v24, 0) <= 65 )
    std::string::operator+=(v22, v34);
  if ( *(_BYTE *)std::string::operator[](v35, 0) != 65 )
    std::string::operator+=(v22, v37);
  if ( "Hello" == "World" )
    std::string::operator+=(v22, v25);
  v19 = *(char *)std::string::operator[](v26, 0);
  if ( v19 - *(char *)std::string::operator[](v30, 0) == 3 )
    std::string::operator+=(v22, v26);
  std::string::operator+=(v22, v25);
  std::string::operator+=(v22, v28);
  if ( *(_BYTE *)std::string::operator[](v29, 0) == 71 )
    std::string::operator+=(v22, v29);
  std::string::operator+=(v22, v27);
  std::string::operator+=(v22, v36);
  std::string::operator+=(v22, v23);
  std::string::operator+=(v22, v31);
  std::string::operator+=(v22, 125);
  std::string::~string(v38);
  std::string::~string(v37);
  std::string::~string(v36);
  std::string::~string(v35);
  std::string::~string(v34);
  std::string::~string(v33);
  std::string::~string(v32);
  std::string::~string(v31);
  std::string::~string(v30);
  std::string::~string(v29);
  std::string::~string(v28);
  std::string::~string(v27);
  std::string::~string(v26);
  std::string::~string(v25);
  std::string::~string(v24);
  std::string::~string(v23);
  std::string::~string(v22);
  return 0;
}
```

Phần đầu của flag được gán vào biến v22, các v.. còn lại đều được gán cho 1 ký tự, và sau đó các phần tiếp theo được tiếp tục gán vào flag nhưng có một vài biến cần điều kiện đúng thì mới được gán

```cpp
  std::allocator<char>::~allocator(&v21);
  if ( *(char *)std::string::operator[](v24, 0) <= 65 )
    std::string::operator+=(v22, v34);
  if ( *(_BYTE *)std::string::operator[](v35, 0) != 65 )
    std::string::operator+=(v22, v37);
  if ( "Hello" == "World" )
    std::string::operator+=(v22, v25);
  v19 = *(char *)std::string::operator[](v26, 0);
  if ( v19 - *(char *)std::string::operator[](v30, 0) == 3 )
    std::string::operator+=(v22, v26);
  std::string::operator+=(v22, v25);
  std::string::operator+=(v22, v28);
  if ( *(_BYTE *)std::string::operator[](v29, 0) == 71 )
    std::string::operator+=(v22, v29);
  std::string::operator+=(v22, v27);
  std::string::operator+=(v22, v36);
  std::string::operator+=(v22, v23);
  std::string::operator+=(v22, v31);
  std::string::operator+=(v22, 125);
```

Lần theo các điều kiện, ta có được phần sau của flag: `97750d5f}`

`picoCTF{wELF_d0N3_mate_97750d5f}`
