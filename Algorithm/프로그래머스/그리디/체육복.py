n = 5
lost = [2, 4]
reserve = [1, 3, 5]

def solution(n, lost, reserve):
    answer = 0

    for i in range(1, n+1):
        # 안 잃어버린경우
        if i not in lost:
            answer += 1
    #잃어버리고, 여분이있는경우
        else:
            if i in reserve:
                answer += 1
                reserve.remove(i)
                lost.remove(i)
    for i in lost: #잃어버리고, 여분이없어 빌려야 하는경우
        if i-1 in reserve:
            answer += 1
            reserve.remove(i-1)
        elif i+1 in reserve:
            answer += 1
            reserve.remove(i + 1)

    return answer

print(solution(n, lost, reserve))