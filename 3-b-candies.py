# Enter your code here. Read input from STDIN. Print output to STDOUT
def candies(kids):
#    diff = [1] * len(kids)
#    pos_adj = 0
#    adj = 0
#    up = 0
#    for i in range(1, len(kids)):
#        if kids[i] > kids[i-1]:
#            diff[i] = diff[i-1] + 1
#            pos_adj = 0
#            up += 1
#        elif kids[i] < kids[i-1]:
#            pos_adj += 1
#            adj += (pos_adj - up)
#            up = 0
#        else:
#            pos_adj = 0
#            up = 0
#    return sum(diff) + adj

    left = [1] * len(kids)
    for i in range(1, len(kids)):
        if kids[i] > kids[i-1]:
            left[i] = left[i-1] + 1

    right = [1] * len(kids)
    for i in range(len(kids)-2, -1, -1):
        if kids[i] > kids[i+1]: 
            right[i] = right[i+1] + 1

    return sum([max(left[i], right[i]) for i in range(len(kids))])
    
c = int(raw_input().strip("\n"))
kids = []
for i in range(c):
    kids.append(int(raw_input().strip("\n")))

print(candies(kids))


# test_case
4
1
2
3
4

4
4
3
2
1

4
1
2
1
2

4
1
5
9
3

4
9
5
1
2
