Web đăng nhập điền tk mk "Chỉ được dùng chữ và số"

![image](https://github.com/user-attachments/assets/91eae849-8b2a-4f8e-9cc2-d3b33e6f949d)

Nếu nhập kí tự đặc biệt sẽ ra

![image](https://github.com/user-attachments/assets/d9403522-591e-410e-b230-084eab4ee04b)

Inspect trang này sẽ thấy 1 phần code js trong source và 1 phần trong secure.js

function filter(string) {
        filterPassed = true;
        for (let i =0; i < string.length; i++){
          cc = string.charCodeAt(i);
          
          if ( (cc >= 48 && cc <= 57) ||
               (cc >= 65 && cc <= 90) ||
               (cc >= 97 && cc <= 122) )
          {
            filterPassed = true;     
          }
          else
          {
            return false;
          }
        }
        
        return true;
      }
    
      window.username = "-";
      window.password = "-";
      
      usernameFilterPassed = filter(window.username);
      passwordFilterPassed = filter(window.password);
      
      if ( usernameFilterPassed && passwordFilterPassed ) {
      
        loggedIn = checkPassword(window.username, window.password);
        
        if(loggedIn)
        {
          document.getElementById('msg').innerHTML = "Log In Successful";
          document.getElementById('adminFormHash').value = "2196812e91c29df34f5e217cfd639881";
          document.getElementById('hiddenAdminForm').submit();
        }
        else
        {
          document.getElementById('msg').innerHTML = "Log In Failed";
        }
      }
      else {
        document.getElementById('msg').innerHTML = "Illegal character in username or password."
      }

Secure.js:


function checkPassword(username, password)
{
  if( username === 'admin' && password === 'strongPassword098765' )
  {
    return true;
  }
  else
  {
    return false;
  }
}

Phần đầu kiểm tra xem mật khẩu có phải là chữ số, ko có ký tự đặc biệt hay ko rồi sẽ check đến mật khẩu có khớp với điều kiện của secure.js ko

Nhập phần tk và mk của Secure.js vào ta có Flag

FLAG: picoCTF{j5_15_7r4n5p4r3n7_05df90c8}
