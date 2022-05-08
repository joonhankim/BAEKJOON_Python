import sys
import heapq

def dijkstra(start_point,distance):
    q = []

    heapq.heappush(q,(0,start_point))
    distance[start_point] = 0

    while q:
        dis, now = heapq.heappop(q)

        if distance[now] < dis:
            continue
        for i in matrix[now]:
            cost = dis +i[1]

            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q,(cost,i[0]))
    return distance


if __name__ == '__main__':
    v,e = map(int, sys.stdin.readline().split())

    INF = int(1e9)
    start_point = int(sys.stdin.readline())

    matrix = [[] for _ in range(v+1)]

    distance = [INF] * (v+1)

    for _ in range(e):
        x,y,z = map(int, sys.stdin.readline().split())
        matrix[x].append((y,z))

    distance = dijkstra(start_point,distance)
    for i in range(1,v+1):
        if distance[i] == INF:
            print("INF")
        else:
            print(distance[i])
