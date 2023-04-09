import hmac
import hashlib

#Đầu vào: một thông điệp và một khóa
message = "Hello! My name is Thanh Khang."
key= "abracadabra"

#Tin nhắn, khóa của người gửi
message_digest1 = hmac.digest(key=key.encode(), msg=message.encode(), digest="sha3_256")

print("Message Digest 1 : {}".format(message_digest1))

#Tin nhắn, khóa của người nhận 
message_digest2 = hmac.digest(key=key.encode(), msg=bytes(message, encoding="utf-8"), digest=hashlib.sha3_256)

print("Message Digest 2 : {}".format(message_digest2))

#Sử dụng compare để so sánh kết quả thông điệp giữa người gửi và người nhận có giống nhau không?
print("\nIs message digest 1 is equal to message digest 2? : {}".format(hmac.compare_digest(message_digest1, message_digest2)))
