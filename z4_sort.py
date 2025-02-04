"""
Сорт
Дано: список из 10**6 целых чисел, каждое из которых лежит на отрезке [13, 25].
Задача: отсортировать массив наиболее эффективным способом

Комментарий по чему лучший вариант

Если не учитывать универсальную сортировку, то сортировка подсчетом в данном случае лучший вариант,
хуже себя показывает быстрая сортировка

"""

import random
import time

def counting_sort(container):    # O(n+k) диапазон значений не большой и ограничен
    if len(container) == 0:
        return container

    max_num = container[0]
    for i in container:
        if i > max_num:
            max_num = i

    list_counts = [0] * (max_num + 1)

    for num in container:
        list_counts[num] += 1

    j = 0
    list_sorted = [0] * len(container)
    for el in range(len(list_counts)):
        while list_counts[el] > 0:
            list_sorted[j] = el
            j += 1
            list_counts[el] -= 1
    return list_sorted

def quick_sort(container):  # O(nlogn) - метод сам по себе медленее
    if len(container) > 1:
        first_elem = container[0]

        left = [x for x in container if x < first_elem]
        middle = [x for x in container if x == first_elem]
        right = [x for x in container if x > first_elem]

        return quick_sort(left) + middle + quick_sort(right)
    return container

def universal_sort(container):
    return sorted(container)




if __name__ == '__main__':
    list_random = [random.randint(13, 25) for _ in range(10**6)]
    # list_random = [random.randint(13, 25) for _ in range(15)]
    # list_random = [random.randint(13, 10**4) for _ in range(10**6)]
    # print(list_random)
    start1 = time.time() # counting_sort
    srt_counting_sort = counting_sort(list_random)
    print(srt_counting_sort)
    finish1 = time.time()
    res_counting_sort = finish1 - start1
    start2 = time.time()    # quick_sort
    srt_quick_sort = quick_sort(list_random)
    print(srt_quick_sort)
    finish2 = time.time()
    res_quick_sort = finish2 - start2
    start3 = time.time()    # universal_sort
    srt_universal_sort = universal_sort(list_random)
    print(srt_universal_sort)
    finish3 = time.time()
    res_universal_sort = finish3 - start3

    print(res_counting_sort)
    print(res_quick_sort)
    print(res_universal_sort)
