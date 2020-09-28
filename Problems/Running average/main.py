n = [int(i) for i in list(input())]
print([sum(n[i:i + 2]) / 2 for i in range(len(n) - 1)])
