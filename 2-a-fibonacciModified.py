def mod_fib(t1, t2, n):
    fib_dict = {1: t1, 2:t2}
    for i in range(3, n+1):
        fib_dict[i] = fib_dict[i-1] ** 2 + fib_dict[i-2]
    
    print fib_dict[n]
    return

t0, t1, n = map(int, [i for i in raw_input().split(" ")])
mod_fib(t0, t1, n)
