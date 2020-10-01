def tallest_people(**kwargs):
    res = []
    for i in kwargs.items():
        if i[1] == max(kwargs.values()):
            res.append(i)
    for name, h in sorted(res):
        print(f'{name} : {h}')

    # print("\n".join(sorted(f"{i} : {j}" for i, j in kwargs.items() if j == max(kwargs.values()))))
