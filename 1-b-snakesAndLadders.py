def snakesAndLadders(snakes, ladders):
    queue, queue2, seen = [1], [], set([])
    action = 0
    while queue:
        while queue:
            if 100 in queue:
                print action
                return
            focus = queue.pop(0)
            if focus > 100:
                print -1
                return
            for i in range(1, 7):
                if focus+i in ladders and ladders[focus+i] not in seen and focus+i not in seen:
                    seen.add(ladders[focus+i])
                    seen.add(focus+i)
                    queue2.append(ladders[focus+i])
                elif focus+i in snakes and snakes[focus+i] not in seen and focus+i not in seen:
                    seen.add(snakes[focus+i])
                    seen.add(focus+i)
                    queue2.append(snakes[focus+i])
                elif focus+i not in seen:
                    queue2.append(focus+i)
                    seen.add(focus+i)
        # print(queue, queue2, seen)
        action += 1
        queue, queue2 = queue2, queue
    print -1

q = int(raw_input().strip())
for query in range(q):
    ladders_count = int(raw_input().strip())
    ladders = {}
    for i in range(ladders_count):
        start, end = map(int, raw_input().strip().split(" "))
        ladders[start] = end
    snakes_count = int(raw_input().strip())
    snakes = {}
    for i in range(snakes_count):
        start, end = map(int, raw_input().strip().split(" "))
        snakes[start] = end
    # print(query, ladders_count, ladders, snakes_count, snakes)
    snakesAndLadders(snakes, ladders)

test_case:

2
1
1 100
0
1
3 90
7
99 10
97 20
98 30
96 40
95 50
94 60
93 70
