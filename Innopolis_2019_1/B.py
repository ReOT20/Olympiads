def repl(x, y):
    i = 0
    count = 0
    while i < len(y):
        if x[i] != y[i]:
            count += 1
        i += 1
    return count


def rec(n, arr, maxlen, minlen, minarr, replcount):
    inf = float("inf")
    minreplin = inf
    minindex = 0
    i = 0
    while i < len(minarr):
        j = 0
        now = 0
        while j < n:
            if j == minarr[i]:
                j += 1
                continue
            now += repl(arr[j], arr[minarr[i]])
            j += 1
        i += 1
    if now < minreplin:
        minreplin = now
        minindex = i
    i = 0
    oldminlen = minlen
    oldmaxlen = maxlen
    maxlen = 0
    minlen = inf
    minarr = []
    while i < n:
        if len(arr[i]) == oldminlen:
            del arr[i]
            n -= 1
        else:
            arr[i] = arr[i][3::]
            if len(arr[i]) > maxlen:
                maxlen = len(arr[i])
            if len(arr[i]) < minlen:
                minlen = len(arr[i])
                minarr = [i,]
            elif len(arr[i]) == minlen:
                print(minarr)
                minarr.append[i]
            i+=1
    if oldmaxlen < 3:
        return replcount + minreplin
    else:
        return rec(n, arr, maxlen, minlen, minarr, replcount + minreplin)
         



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
        minar.append[i]
    arr.append(now)
    i += 1
print(rec(n, arr, maxlen, minlen, minar, 0))