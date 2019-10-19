import queue

def max(a, b):
    if(a >= b):
        return a
    else:
        return b

def output(dist, farthest_node, parents):
    with open('output.txt', 'w') as output:
        output.write(str(dist) + '\n')
        node = farthest_node
        output.write(str(farthest_node) + ' ')
        while parents[node] != -1:
            output.write(str(parents[node] + 1) + ' ')
            node = parents[node]

def bfs(graph, start):
    q = queue.Queue()
    q.put(start)
    d, used, p = [-1]*nodes, [False]*nodes, [None]*nodes
    d[start] = 0
    used[start] = True
    p[start] = -1
    while not q.empty():
        node = q.get()
        for to in graph[node]:
            if not used[to]:
                used[to] = True
                d[to] = d[node] + 1
                p[to] = node
                q.put(to)
    farthest_node = start
    for node in range(nodes):
        if d[node]>d[farthest_node]:
            farthest_node = node
    output(d[farthest_node], farthest_node, p)

with open('input.txt', 'r') as input:
    edges, start = map(int, input.readline().split())
    start = start - 1
    nodes = 0
    pair = [] * edges
    for i in range(edges):
        f, t = map(int, input.readline().split())
        pair.append((f, t))
        nodes = max(nodes, max(pair[i][0], pair[i][1]))
    graph = []
    for node in range(nodes):
        graph.append([])
    for i in range(edges):
        graph[pair[i][0]-1].append(pair[i][1]-1)

bfs(graph, start)
