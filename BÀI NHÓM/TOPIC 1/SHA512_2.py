Python 3.11.2 (tags/v3.11.2:878ead1, Feb  7 2023, 16:38:35) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #hashlib là mô đun chứa giao diện cho các thuật toán băm phổ biến
>>> import hashlib
>>> #Dùng def để khai báo hàm
>>> def hash_SHA512(data):
...     #Chuyển đổi dữ liệu đầu vào sang dạng bytes, sử dụng encode
...     data = data.encode('utf-8')
...     #Khởi tạo đối tượng SHA512 với sự hỗ trợ mô đun hashlib
...     hash_object = hashlib.sha512()
...     #Cập nhật dữ liệu input cho đối tượng
...     hash_object.update(data)
...     #Chuyển đổi giá trị băm sang dạng hex
...     hash_value = hash_object.hexdigest()
...     #Trả về giá trị
...     return hash_value
... 
>>> data = "Tran Phong Phu"
>>> #Gán hàm khai báo hash_SHA512(data) cho hash_value
>>> hash_value = hash_SHA512(data)
>>> print(hash_value)
6f31a4543d489d604ebdf6923e77b884c0bbc7c826539f3ad1af7840f97c91457b4193f354175ee5109a4986f2e0364968dcee2f9e34f064ad481754d0ff9b0c
