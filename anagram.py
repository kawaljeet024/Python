str1 = "listen"
str2 = "silent"
str1a = sorted(str1)
str2a = sorted(str2)
print(str1a)
print(str2a)
str1b = ''.join(str1a)
str2b = ''.join(str2a)
print(str1b)
print(str2b)
if (str1b == str2b):
    print("these are anagrams")
else:
    print("these are not anagrams")
