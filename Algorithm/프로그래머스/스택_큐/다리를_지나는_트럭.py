bridge_length, weight = 100, 100
truck_weights = [10,10,10,10,10,10,10,10,10,10]
def solution(bridge_length, weight, truck_weights):
    time = 0
    queue = [0] * bridge_length
    while queue:
        time+=1
        queue.pop(0)
        if truck_weights:
            if sum(queue) + truck_weights[0] <=weight:
                queue.append(truck_weights.pop(0))
            else:
                queue.append(0)
    return time

print(solution(bridge_length,weight,truck_weights))