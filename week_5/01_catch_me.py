from collections import deque

c = 180000
b = 10000


def catch_me(cony_loc, brown_loc):
    time = 0
    queue = deque()
    queue.append((brown_loc, 0))  # 위치 + 시간
    visited = [{} for _ in range(200001)]#  브라운의 방문여부를 저장

#코니                         for문        0       1      2
    while cony_loc <= 200000:    #코니 [0,11] [1,12]  [2,13]
        cony_loc += time
        if cony_loc>20000:
            return -1
        if time in visited[cony_loc]:
            return time

#브라운
        for i in range(0, len(queue)):
            current_position, current_time = queue.popleft()

            new_time = current_time + 1# t=1

            new_position = current_position - 1 # cur -1 일때
            if 0 <= new_position <= 200000:
                visited[new_position][new_time] = None
                queue.append((new_position, new_time))

            new_position = current_position + 1 # cur +1 일때
            if 0 <= new_position <= 200000:
                visited[new_position][new_time] = None
                queue.append((new_position, new_time))

            new_position = current_position * 2 # cur * 2 일때
            if 0 <= new_position <= 200000:
                visited[new_position][new_time] = None
                queue.append((new_position, new_time))

        time += 1

    return -1

print(catch_me(c, b))  # 5가 나와야 합니다!
