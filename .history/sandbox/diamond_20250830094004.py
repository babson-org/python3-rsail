height = 7
middle = 7 // 2

for i in range(height):

    s1 = abs(middle - i)
    s2 = max(0, (i > 0) * (2 * (middle - s1) - 1))
    
    print(' ' * s1 + '*' + ' ' * s2 + '*' * (s2 > 0))


for i in range(height):
    # Calculate spaces before the first star
    spaces_before = abs(middle - i)
    
    # Calculate spaces between stars
    if i <= middle:
        spaces_between = i * 2 - 1
    else:
        spaces_between = (height - i - 1) * 2 - 1

    # Print spaces before first star
    for _ in range(spaces_before):
        print(' ', end='')

    # Print first star
    print('*', end='')

    # Print spaces between stars and second star if needed
    if spaces_between > 0:
        for _ in range(spaces_between):
            print(' ', end='')
        print('*', end='')

    # Move to the next line
    print()