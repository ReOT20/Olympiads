def repl(x, y, minlen):
    i = 0
    count = 0
    while i < len(y) and i < minlen and i < len(x):
        if x[i] != y[i]:
            count += 1
        i += 1
    return count


def rec(n, arr, maxlen, minlen, replcount):
    inf = float("inf")
    minreplin = inf
    i = 0
    now = 0
    while i < n:
        j = 0
        now = 0
        while j < n:
            if j == i:
                j += 1
                continue
            now += repl(arr[j], arr[i], minlen)
            j += 1
        if now < minreplin:
            minreplin = now
        i += 1
    if minreplin == inf:
        minreplin = 0
    i = 0
    oldminlen = minlen
    maxlen = 0
    minlen = inf
    while i < n:
        if len(arr[i]) == oldminlen:
            del arr[i]
            n -= 1
        else:
            arr[i] = arr[i][oldminlen::]
            if len(arr[i]) > maxlen:
                maxlen = len(arr[i])
            if len(arr[i]) < minlen:
                minlen = len(arr[i])
            i+=1
    if len(arr) < 2:
        return replcount + minreplin
    else:
        return rec(n, arr, maxlen, minlen, replcount + minreplin)     



n = int(input())
i = 0
arr = []
inf = float("inf")
maxlen = 0
minlen = inf
minar = []
while i < n:
    now = input()
    if len(now) > maxlen:
        maxlen = len(now)
    if len(now) < minlen:
        minlen = len(now)
        minar = [i]
    elif len(now) == minlen:
        minar.append(i)
    arr.append(now)
    i += 1
print(rec(n, arr, maxlen, minlen, 0))