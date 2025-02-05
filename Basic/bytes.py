

# Python-এ bytes হলো immutable (পরিবর্তন করা যায় না) বাইনারি ডাটা টাইপ

# এটি সাধারণত বাইনারি ডাটা সংরক্ষণ, নেটওয়ার্ক ডাটা ট্রান্সমিশন, ফাইল I/O অপারেশন, এবং এনকোডিং/ডিকোডিং এর জন্য ব্যবহৃত হয়।

# একটি bytes অবজেক্ট আসলে একটি ইমিউটেবল অ্যারে, যেখানে প্রতিটি উপাদান 0 থেকে 255 এর মধ্যে থাকে। 



# data = b"Hello"
# print(data)          # Output: b'Hello'
# print(type(data))    # Output: <class 'bytes'>


# data = bytes([65, 66, 67])  
# print(data)          # Output: b'ABC'
# print(data[0])       # output: 65
# # print( )
# print(data.split())  # Output: [b'ABC']

text = "বাংলা"
# print(type(text))
data = text.encode("utf-8")   # UTF-8 encoding
print(data)          # Output: b'\xe0\xa6\xac\xe0\xa6\xbe\xe0\xa6\x82\xe0\xa6\xb2\xe0\xa6\xbe'
# print(type(data))

# data = b'\xe0\xa6\xac\xe0\xa6\xbe\xe0\xa6\x82\xe0\xa6\xb2\xe0\xa6\xbe'
# text = data.decode("utf-8")   # UTF-8 decoding
# print(text)  # Output: বাংলা

# ✅ বাইনারি ফাইল (ইমেজ, অডিও, ভিডিও) হ্যান্ডল করার জন্য।
# ✅ নেটওয়ার্কিং-এ ডাটা ট্রান্সমিশনের জন্য।
# ✅ এনকোডিং ও ডিকোডিং প্রসেসের জন্য।
# ✅ স্টোরেজ ও মেমোরি ব্যবহারে কার্যকর।




# bytes হচ্ছে Python-এ ইমিউটেবল বাইনারি ডাটা টাইপ, যা বিশেষ করে ফাইল হ্যান্ডলিং, নেটওয়ার্কিং ও এনকোডিং/ডিকোডিং-এ ব্যবহৃত হয়। 
# এটি string-এর মতোই আচরণ করে, তবে ইমিউটেবল এবং শুধুমাত্র byte values (0-255) ধারণ করে।
