height = 7
peak = 7 // 2

for i in range(height):
    s1 = abs(peak - i)
    s2 = (i > 0) * (2 * i - 1)
    
    print('_' * s1, end = '*')
    print('_' * s2, end = '*')
    print()