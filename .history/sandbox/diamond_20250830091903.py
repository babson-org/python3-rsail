height = 7
peak = 7 // 2

for i in range(height):
    s1 = abs(peak - i)
    s2 = (i > 0) * (2 * i - 1)
    for space in s1:
        print('_', end = '')
    print('*')
    for space in s2:
        print('_', end = '')
    for mark in range([1 if s2 !=0 else 0])