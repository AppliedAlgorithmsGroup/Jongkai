def equal(n, cookies):
    cookies.sort()
    good = cookies[-1]*len(cookies)
    
    for case in range(5):
        diff_cookies = [i - cookies[0] + case for i in cookies]
        cookies_inc = [5, 2, 1]
    
        op = 0
        for intern in diff_cookies:
            inc = 0
            while intern > 0:
                if intern < cookies_inc[inc]:
                    inc += 1
                count, intern = divmod(intern, cookies_inc[inc])
                op += count
        good = op if op < good else good    
        # print(diff_cookies[0], good)
    print(good)

q = int(raw_input().strip())
for query in range(q):
    n = int(raw_input().strip())
    if n == 0:
        print(0)
        continue
    cookies = map(int,raw_input().strip().split(' '))
    equal(n, cookies)



# def equal(n, cookies):
#     cookies.sort()
#     diff_cookies = [i - cookies[0] for i in cookies]
#     cookies_inc = [5, 2, 1]
    
#     op = 0
#     for intern in diff_cookies:
#         inc = 0
#         while intern > 0:
#             if intern < cookies_inc[inc]:
#                 inc += 1
#             count, intern = divmod(intern, cookies_inc[inc])
#             op += count
#     print(op)


# def equal(n, cookies):
#     cookies.sort()
#     diff_cookies = reduce(lambda x, y: x+y, [i - cookies[0] for i in cookies])
#     cookies_inc = [5, 2, 1]
    
#     op, inc = 0, 0
#     while diff_cookies > 0:
#         if diff_cookies >= cookies_inc[inc]:
#             count, diff_cookies = divmod(diff_cookies, cookies_inc[inc])
#             op += count
#         inc += 1
#     print(op)
