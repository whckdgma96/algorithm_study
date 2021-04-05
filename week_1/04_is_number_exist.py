input = [3, 5, 6, 1, 2, 4]


def is_number_exist(number, array):
    for element in array:  # array의 길이만큼
        if number == element:  # 비교연산 1번
            return True  # N * 1

    return False


result = is_number_exist(4, input)
print(result)
