def palind(r):
    e = len(r) - 1
    s = 0
    while(s>e):
        if r(e) != r(s):
            return False
        s += 1
        e -= 1
r = (1,2,3,3,4,5)

if palind(r):
    print("The tuple is flip-flop")
else:
    print("The tuple is not flip-flop")