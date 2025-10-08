from collections import defaultdict, deque

def solution(tickets):
    ticket_list = defaultdict(list)
    for ticket in tickets:
        ticket_list[ticket[0]].append(ticket[1])
    for v in ticket_list.values():
        v.sort(reverse=True)
    route = []
    
    def dfs(airport):
        print(airport)
        while ticket_list[airport]:
            next = ticket_list[airport].pop()
            dfs(next)
        route.append(airport)
        
    dfs('ICN')
    return route[::-1]
   