Python 3.11.2 (tags/v3.11.2:878ead1, Feb  7 2023, 16:38:35) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #hashlib là mô đun chứa giao diện cho các thuật toán băm phổ biến
>>> import hashlib
>>> #Dùng def để khai báo hàm
>>> def hash_MD5(data):
...     #Chuyển đổi dữ liệu đầu vào sang dạng bytes, sử dụng encode
...     data = data.encode('utf-8')
...     #Khởi tạo đối tượng MD5 với sự hỗ trợ mô đun hashlib
...     hash_object = hashlib.md5()
...     #Cập nhật dữ liệu input cho đối tượng
...     hash_object.update(data)
...     #Chuyển đổi giá trị băm sang dạng hex
...     hash_value = hash_object.hexdigest()
...     #Trả về giá trị
...     return hash_value
... 
>>> data = "Tran Thi Thanh Khang"
>>> #Gán hàm khai báo hash_MD5(data) cho hash_value
>>> hash_value = hash_MD5(data)
>>> print(hash_value)
1e67a085b7965a0d471aeac94d1f6811
