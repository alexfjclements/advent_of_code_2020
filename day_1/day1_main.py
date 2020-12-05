from day_1.day1_input import day1_input_data

result = []

# Part 1
# for x in day1_input_data:
#     for y in day1_input_data:
#         if x != y and x + y == 2020:
#             result.append(x*y)
#
# if result[0] == result[1]:
#     print(result[0])
# else:
#     print('Error')

# Part 2
for x in day1_input_data:
    for y in day1_input_data:
        if x != y:
            for z in day1_input_data:
                if z != y and x + y + z == 2020:
                    result.append(x*y*z)

if result[0] == result[1]:
    print(result[0])
else:
    print('Error')
