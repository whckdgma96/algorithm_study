clothes= [["yellowhat", "headgear"],
          ["bluesunglasses", "eyewear"],
          ["green_turban", "headgear"]]
def solution(clothes):
    clothes_type = {}
    for cloth, type in clothes:
        if type not in clothes_type:
            clothes_type[type] = 2
        else:
            clothes_type[type] += 1

    station = 1
    for num in clothes_type.values():
        station *= num
    return station - 1


print(solution(clothes))