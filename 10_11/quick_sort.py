"""
퀵 솔트

[4, 3, 2, 7, 6, 5]

1차 정렬)
    list = [4, 3, 2, 7, 6, 5]
    pivot = 4
    low_list = [2, 3]
    high_list = [5, 6, 7]

    return [2, 3, 4, 5, 6, 7]

2차 정렬)
    list = [3, 2]
    pivot = 3
    low_list = [2]
    high_list = []

    return quick_sort(low) + [pivot] + quick_sort(high)
    return [2, 3]


3차 정렬)
    list = [2]
    return [2]

4차 정렬)
    list = []
    return []

5차 정렬)
    list = [7, 6, 5]
    pivot = 7
    low_list = [5, 6]
    high_list = []

    return [5, 6, 7]

6차 정렬)
    quick_sort(low_list)
    list = [6, 5]

    pivot = 6
    low_list = [5]
    high_list = []

    return [5, 6]

"""


def quick_sort(unsorted_list: list) -> list:
    if len(unsorted_list) <= 1:
        return unsorted_list

    pivot = unsorted_list[0]
    low = []
    high = []

    for i in range(1, len(unsorted_list), 1):
        val = unsorted_list[i]
        if val >= pivot:
            high.append(val)
        else:
            low.append(val)

    return quick_sort(low) + [pivot] + quick_sort(high)


if __name__ == "__main__":
    test_case = [4, 3, 2, 7, 6, 5]
    sorted_array = quick_sort(test_case)
    print("정렬된 배열:", sorted_array)
