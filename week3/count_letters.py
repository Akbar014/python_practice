

s = input()
frq = [0] * 26

for i in s:
    frq[ord(i) - ord('a')] += 1


# for count in frq:
#     print(count)

for i in range(len(frq)):
    if(frq[i]>0):
        print(f"{chr(i + ord('a'))} : {frq[i]}")


