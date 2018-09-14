str1 = "abc 44 ed 22 fg 12 xyz 200"
newstr1 = str1.split(" ")
print(newstr1)

list1 = []
for ele in newstr1:
    if ele.isdigit():
        list1.append(ele)
print(list1)
list1.sort(key=int)  # key=int is because it was taking is as string , now every str char is taken as integer value
print(list1)
print(list1[len(list1) - 1])
