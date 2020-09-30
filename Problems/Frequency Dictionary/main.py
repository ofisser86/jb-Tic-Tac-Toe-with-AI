# put your python code here
words_line = input().lower().split()
words = {k: words_line.count(k) for k in words_line}
for k, v in words:
    print(k, v)
