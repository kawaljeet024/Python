import array
arr = [1, 0, 1, 1, 0, 1, 0, 1, 0]
n = len(arr)


def segregate(arr, n):
    count = 0

    for i in range(0, n):
        if (arr[i] == 0):
            count = count + 1
    for i in range(0, count):
        arr[i] = 0
    for i in range(count, n):
        arr[i] = 1


def print_arr(arr, n):
    print("array after segregation is", end=" ")

    for i in range(0, n):
        print(arr[i], end=" ")


segregate(arr, n)
print_arr(arr, n)
