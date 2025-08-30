height = 7
middle = 7 // 2

for i in range(height):

    s1 = abs(middle - i)
    s2 = max(0, (i > 0) * (2 * (middle - s1) - 1))
    
    print(' ' * s1 + '*' + ' ' * s2 + '*' * (s2 > 0))



        

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

height = 7
middle = 7 // 2


#top half
for i in range(middle + 1):

    spaces_before = middle - i
    spaces_between = i * 2 - 1

    print(' ' * spaces_before, end = '*')

    if spaces_between > 0: print(' ' * spaces_between, end = '*')
    print()

#bottom half
for i in range(middle - 1, -1, -1):

    spaces_before = middle - i
    spaces_between = i * 2 - 1

    print(' ' * spaces_before, end = '*')

    if spaces_between > 0: print(' ' * spaces_between, end = '*')
    print()
