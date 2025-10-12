import heapq

def solution(scoville, K):
    heapq.heapify(scoville)
    count = 0
    while True:
        if len(scoville) == 1 and scoville[0] < K:
            return -1
        not_hot = heapq.heappop(scoville)
        if not_hot >= K:
            return count
        little_hot = heapq.heappop(scoville)
        new_hot = not_hot + 2 * little_hot
        count += 1
        heapq.heappush(scoville, new_hot)
    