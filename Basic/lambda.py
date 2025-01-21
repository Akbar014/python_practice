

# x = lambda a, b : a * b
# print(x(5, 6))


s = "the sky is blue"
s1 = s.split()
s2 = []

# print(len(s1)) 
for x in range(len(s1)-1,0,-1):
    # print(s1[x])
    s2.append(s1[x-1])


res = ' '.join(s2)
print(res)



# print(s.split())