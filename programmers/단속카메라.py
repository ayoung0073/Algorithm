import heapq
def solution(routes):
    routes.sort(key = lambda x : x[0])       
    
    arr = []
    for route in routes:
        start, end = route
        if arr and arr[0][1] >= start:
            if end < arr[0][1]:
                heapq.heappop(arr)
                heapq.heappush(arr, ((-1)*start, end))
        else:
            heapq.heappush(arr, ((-1)*start, end))
    return len(arr)
