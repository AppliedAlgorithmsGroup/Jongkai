def even_tree(graph):    
    # print(graph)
    seen = {"1":1}
    print DFS(graph, "1", seen)[1]
    return

def DFS(graph, root, seen):
    below, cut = 0, 0
    for i in graph[root]:
        if i not in seen:
            seen[i] = 1
            new_below, new_cut = DFS(graph, i, seen)
            if new_below % 2 == 0 and new_below > 0:
                cut += 1
                new_below = 0
            below += new_below
            cut += new_cut
    return(below+1, cut)


n, m = raw_input().strip("\n").split(" ")
graph = {}
for edge in range(int(m)):
    v1, v2 = raw_input().strip("\n").split(" ")
    if v1 not in graph:
        graph[v1] = [v2]
    else: graph[v1].append(v2)
    if v2 not in graph:
        graph[v2] = [v1]
    else: graph[v2].append(v1)

if len(graph.keys()) % 2 == 1:
    print(0)
else:
    even_tree(graph)

