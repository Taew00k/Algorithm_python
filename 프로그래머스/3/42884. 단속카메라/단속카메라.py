def solution(routes):
    routes.sort(key = lambda x: x[1])
    camera = -30001
    count = 0
    print(routes)
    
    for route in routes:
        start, end = route
        
        if camera < start:
            count += 1
            camera = end
    return count
    