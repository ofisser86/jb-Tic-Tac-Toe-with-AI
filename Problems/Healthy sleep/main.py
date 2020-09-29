# a, b, h = [int(input()) for i in range(3)]
# print(["Deficiency", 'Normal', "Excess"][sorted([a, b, h]).index(h)])
a, b, h = [int(input()) for i in range(3)]
if a <= h <= b:
    print('Normal')
elif h > b:
    print("Excess")
else:
    print("Deficiency")
