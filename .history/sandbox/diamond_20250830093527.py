height = 7
peak = 7 // 2

for i in range(height):
    s1 = abs(peak - i)
    s2 = max(0, (i > 0) * (2 * (peak - s1) - 1))
    
    print('_' * s1 + '*' + '_' * s2 + '*' * (s2 > 0))