from collections import deque
price = [1,2,3,2,3]

def solution(prices):
    answer = []

    queue = deque(prices)

    while queue:
        price = queue.popleft()
        time = 0
        for n in queue:
            time += 1
            if price > n:
                break
        answer.append(time)
    return answer



print(solution(price))