# put your python code here
days = int(input())
total_food = int(input())
flight = int(input())
bed = int(input())

print(days * total_food + (flight * 2) + (days - 1) * bed)
