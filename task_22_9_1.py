# Ввод данных и преобразование последовательности в список:

a = input('Введите последовательность чисел через пробел: ')
element_1 = int(input('Введите любое число: '))
array = list(map(int, a.split()))

if element_1 <= min(array) or element_1 >= max(array):
    print("Ошибка: введенное число не входит в диапазон значений списка.")
    exit()

# Проверяем результат:
print("-----------")
print(array)
print("-----------")
print(element_1)

# Проводим сортировку с помощью алгоритма быстрой сортировки:
import random

def qsort_random(array, left, right):
    p = random.choice(array[left:right + 1])
    i, j = left, right
    while i <= j:
        while array[i] < p:
            i += 1
        while array[j] > p:
            j -= 1
        if i <= j:
            array[i], array[j] = array[j], array[i]
            i += 1
            j -= 1

    if j > left:
        qsort_random(array, left, j)
    if right > i:
        qsort_random(array, i, right)

qsort_random(array, 0, (len(array)-1))
# Проверяем результат:
print("-----------")
print(array)

# Устанавливается индекс элемента в отсортированном списке,
# который меньше введенного пользователем числа,
# а следующий за ним больше или равен этому числу с помощью алгоритма двоичного поиска:

def binary_search(array, element):
    left, right = 0, len(array) - 1
    while left <= right:
        middle = (left + right) // 2
        if array[middle] < element:
            left = middle + 1
        else:
            right = middle - 1

    return right

element_1_index = binary_search(array, element_1)
print("-----------")
print("Индекс искомого элемента: ", element_1_index)
