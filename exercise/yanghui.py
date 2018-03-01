def o():
	L = [1]
    yield L
    L = [1, 1]
    yield L
    N = [1]
    while Ture:
        n = 0
        while n < len(L)-1:
            N.append(L(n)+L(n+1))
        N.append(1)
        L = N
        yield L
t = o()
for i in t:
	print(t)
input()