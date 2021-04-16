people = [70, 50, 80, 50]
limit = 100
def solution(people, limit):
    answer = 0
    people.sort()
    cnt = 0

    first_index = 0
    last_index = len(people) - 1

    while first_index < last_index:
        if people[first_index] + people[last_index] <= limit:
            first_index += 1
        last_index -= 1
        cnt += 1

    if first_index == last_index:
        cnt += 1

    return cnt

print(solution(people,limit))