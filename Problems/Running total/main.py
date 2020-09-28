n = [int(i) for i in list(input())]
print([sum(n[:i + 1]) for i in range(len(n))])
