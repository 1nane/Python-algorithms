'''В массиве случайных целых чисел поменять
местами минимальный и максимальный элементы.'''

arr = [int(i) for i in input('Введите элементы массива через пробел: ').split()]
i_min = 0
i_max = 0
for i in range(len(arr)):
    if arr[i] < arr[i_min]:
        i_min = i
    elif arr[i] > arr[i_max]:
        i_max = i

arr[i_min], arr[i_max] = arr[i_max], arr[i_min]
print(arr)