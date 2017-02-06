def BFS(n, s):
    retList = [-1] * n
    retList[s-1] = 0
    queue = [s]

    while queue:
        focus = queue.pop(0)
	if focus in edges:
	    for node in edges[focus]:
               	if retList[node-1] == -1:
			retList[node-1] = retList[focus-1] + 6
			queue.append(node)

    retList.pop(s-1)
    print(" ".join([str(i) for i in retList]))


raw_input = open("case5.txt", "r")
q = int(raw_input.readline().strip())
for query in range(q):
    n, m = map(int,raw_input.readline().strip().split(' '))
    edges = {}
    for i in range(m):
        v1, v2 = map(int, raw_input.readline().strip().split(" "))
        if v1 == v2:
            continue
        edges[v1] = edges.get(v1, [])
        if v2 in edges[v1]:
            continue
        edges[v1].append(v2)
        edges[v2] = edges.get(v2, [])
        edges[v2].append(v1)
    s = int(raw_input.readline().strip())
    # print(q, n, m, edges, s)
    if m == 0:
        print(" ".join(["-1"]* (n-1)))
        continue
    BFS(n, s)
