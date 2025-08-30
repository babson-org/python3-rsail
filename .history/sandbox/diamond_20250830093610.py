height = 7
middle = 7 // 2

for i in range(height):
    s1 = abs(middle - i)
    s2 = max(0, (i > 0) * (2 * (middle - s1) - 1))
    
    print(' ' * s1 + '*' + ' ' * s2 + '*' * (s2 > 0))