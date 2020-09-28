lines = int(input())
winners = []
for _ in range(lines):
    data = input().split()
    if 'win' in data:
        winners.append(data[0])
print(winners)
print(len(winners))
