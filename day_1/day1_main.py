from day_1.day1_input import day1_input_data

result = []

for x in day1_input_data:
    for y in day1_input_data:
        if x != y and x + y == 2020:
            result.append(x*y)

if result[0] == result[1]:
    print(result[0])
else:
    print('Error')