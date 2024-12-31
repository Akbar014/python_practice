

# s = input()

# result = ''

# for i in range(len(s)):
#     if(ord(s[i]) >= 65 and ord(s[i]) <= 90 ):
#         char = chr(ord(s[i]) + 32)
#         result += char
#     elif(ord(s[i]) >= 97 and ord(s[i]) <= 122 ):
#         char = chr(ord(s[i]) - 32)
#         result += char
#     elif(s[i] == ',' ):
#         result += ' '
#     else:
#         result += s[i]

# print(result)

# ............................................ another approach to solve ...............................................

s = input()

result = s.swapcase().replace(',', ' ')

print(result)