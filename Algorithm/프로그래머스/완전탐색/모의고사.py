answers = [1, 3, 2, 4, 2]


def solution(answers):
    answer = []
    a1 = [1, 2, 3, 4, 5]  # 5
    a2 = [2, 1, 2, 3, 2, 4, 2, 5]  # 8
    a3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]  # 10
    correct_1, correct_2, correct_3 = 0, 0, 0
    for i in range(len(answers)):
        s1 = i % 5
        s2 = i % 8
        s3 = i % 10

        if a1[s1] == answers[i]:
            correct_1 += 1
        if a2[s2] == answers[i]:
            correct_2 += 1
        if a3[s3] == answers[i]:
            correct_3 += 1
    k = max(correct_1, correct_2, correct_3)

    if k == correct_1:
        answer.append(1)
    if k == correct_2:
        answer.append(2)
    if k == correct_3:
        answer.append(3)

    return answer


print(solution(answers))
