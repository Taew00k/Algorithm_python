def solution(bridge_length, weight, truck_weights):
    bridge = [0] * bridge_length
    count = 0
    while True:
        if truck_weights == [] and bridge == [0] * bridge_length:
            return count
        count += 1
        bridge.pop(0)
        if len(truck_weights) > 0 and sum(bridge) + truck_weights[0] <= weight:
            bridge.append(truck_weights.pop(0))
        else:
            bridge.append(0)
        
        