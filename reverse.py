str1 = "kawal"


def reverse(str1):
    revstring = ''
    index = (len(str1))
    # print(len(str1))
    while index > 0:
        revstring += str1[index - 1]
        # print(revstring)
        index = index - 1
        # print(index)
    return revstring


print(reverse(str1))
