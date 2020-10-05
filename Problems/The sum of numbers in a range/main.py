def range_sum(numbers, start, end):
    result = 0
    for i in numbers:
        if start <= i <= end:
            result += i
    return result


input_numbers = [int(i) for i in input().split()]  # ...
a, b = [int(i) for i in input().split()]  # ...
print(range_sum(input_numbers, a, b))
