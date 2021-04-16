current_r, current_c, current_d = 7, 4, 0
current_room_map = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 1, 1, 1, 1, 0, 1],
    [1, 0, 0, 1, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]
#0: 청소할곳
#1: 청소 못하는곳
#2: 청소한곳
#     북 동  남  서
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]
def get_d_index_when_rotate_to_left(d):
    return (d+3) %4
def get_d_index_when_go_back(d):
    return (d+2) %4

def get_count_of_departments_cleaned_by_robot_vacuum(r, c, d, room_map):
    n = len(room_map)
    m= len(room_map[0])
    count_of_departments_cleaned = 1
    room_map[r][c] = 2
    queue = list([[r,c,d]])
    while queue:
        r,c,d = queue.pop(0)
        tem_d = d
        for i in range(4):
            tem_d = get_d_index_when_rotate_to_left(tem_d)
            new_r, new_c =r + dr[tem_d], c + dc[tem_d]
            if 0<= new_c < n and 0<= new_c<m and room_map[new_r][new_c]==0:
                count_of_departments_cleaned += 1
                room_map[new_r][new_c] =2
                queue.append([new_r, new_c,tem_d])
                break
            elif i == 3:
                new_r, new_c = r+ dr[get_d_index_when_go_back(tem_d)], c + dc[get_d_index_when_go_back(tem_d)]
                queue.append([new_r, new_c, tem_d])
                if current_room_map[new_r][new_c] ==1:
                    return count_of_departments_cleaned

    return
# 57 가 출력되어야 합니다!
print(get_count_of_departments_cleaned_by_robot_vacuum(current_r, current_c, current_d, current_room_map))