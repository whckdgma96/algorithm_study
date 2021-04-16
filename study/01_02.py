input = "011110"


def find_count_to_turn_out_to_all_zero_or_all_one(string):
    count_zero_to_one = 0
    count_one_to_zero = 0
    if string[0] == '0':
        count_zero_to_one += 1
    elif string[0] == '1':
        count_one_to_zero += 1

    for i in range(len(string)-1):
        if string[i] != string[i+1]:
            if string[i+1] == '1':
                count_one_to_zero += 1
            elif string[i+1] == '0':
                count_zero_to_one += 1


    return print(count_one_to_zero, count_zero_to_one)


result = find_count_to_turn_out_to_all_zero_or_all_one(input)
print(result)