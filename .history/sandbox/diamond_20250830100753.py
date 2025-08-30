height = 7
middle = 7 // 2

for i in range(height):

    s1 = abs(middle - i)
    s2 = max(0, (i > 0) * (2 * (middle - s1) - 1))
    
    print(' ' * s1 + '*' + ' ' * s2 + '*' * (s2 > 0))


for i in range(height):

    if (i % (height - 1) == 0):
        print(' ' * middle + '*')
    else:
        print(' ' * abs(middle - i) + '*' + ' ' * (2 * (middle - abs(middle - i)) - 1) + '*')
        

height = 7
middle = height // 2

for i in range(height):
    distance = abs(middle - i)
    spaces_before = distance
    spaces_between = (middle - distance) * 2 - 1

    # Print spaces before first star
    for _ in range(spaces_before):
        print(' ', end='')

    # Always print first star
    print('*', end='')

    # Print inside spaces + second star if needed
    if spaces_between > 0:
        for _ in range(spaces_between):
            print(' ', end='')
        print('*', end='')

    # Move to next line
    print()
