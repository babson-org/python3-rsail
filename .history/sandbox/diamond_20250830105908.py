height = 7
middle = 7 // 2

for i in range(height):
    s1 = abs(middle - i)
    s2 = max(0, (i > 0) * (2 * (middle - s1) - 1))    
    print(' ' * s1 + '*' + ' ' * s2 + '*' * (s2 > 0))







#************************************************

"""
Diamond Printer Program
-----------------------
This program prints a diamond shape made of '*' characters. The height
of the diamond must be an odd number (e.g., 7). The diamond is printed
by splitting it into two halves:
    1. The top half (including the middle line)
    2. The bottom half

We carefully calculate:
    - spaces_before: Number of spaces before the first '*' on each line.
    - spaces_between: Number of spaces between the two '*' characters on each line.
    
For example, with height = 7, the output looks like this:

                    before     between
---*                  3           0  (-1)
--*-*                 2           1
-*---*                1           3
*-----*               0           5
-*---*                1           3
--*-*                 2           1
---*                  3           0  (-1)
"""

height = 7                     # Must be an odd number
middle = height // 2           # Index of the middle row (0-based)

# ------------------ TOP HALF ------------------ #
# This loop prints the top half of the diamond, including the middle row.
for i in range(middle + 1):
    # spaces_before: number of spaces before the first '*'
    # As we go down each row, spaces_before decreases.
    spaces_before = middle - i

    # spaces_between: spaces between the two '*' characters
    # Starts at -1 (for the first row), then 1, 3, 5, ...
    spaces_between = i * 2 - 1

    # Print spaces before the first '*'
    for _ in range(spaces_before):
        print(' ', end='')

    # Always print the first '*'
    print('*', end='')

    # Print the second '*' only if there’s room for it
    if spaces_between > 0:
        # Print the spaces between the two '*'
        for _ in range(spaces_between):
            print(' ', end='')
        # Print the second '*'
        print('*', end='')

    # Move to the next line
    print()

# ------------------ BOTTOM HALF ------------------ #
# This loop prints the bottom half of the diamond.
# Notice the only thing that changes is the range

for i in range(middle - 1, -1, -1):
    # spaces_before increases again as we go downward
    spaces_before = middle - i

    # spaces_between shrinks as we go downward
    spaces_between = i * 2 - 1

    # Print spaces before the first '*'
    for _ in range(spaces_before):
        print(' ', end='')

    # Always print the first '*'
    print('*', end='')

    # Print the second '*' only if there’s room for it
    if spaces_between > 0:
        # Print the spaces between the two '*'
        for _ in range(spaces_between):
            print(' ', end='')
        # Print the second '*'
        print('*', end='')

    # Move to the next line
    print()



     #*********************************************88   

"""
Draws a diamond (or hourglass-like) pattern of '*' characters based on the given height.

For example, for height = 7, the output looks like:

   *          <-- 3 spaces, 1 star
  * *         <-- 2 spaces, 1 star, 1 space, 1 star
 *   *        <-- 1 space,  1 star, 3 spaces, 1 star
*     *       <-- 0 spaces, 1 star, 5 spaces, 1 star
 *   *        <-- symmetric bottom half
  * *        
   *

Key variables:
-------------
height          : total number of rows in the diamond.
middle          : index of the middle row (zero-based).
spaces_before   : number of leading spaces before the first '*'.
spaces_between  : number of spaces between the two '*' on each line.
"""

height = 7
middle = height // 2  # Integer division → middle index, e.g., 7 // 2 = 3

for i in range(height):
    # spaces_before = distance from the middle row
    # Top half: decreases as we go down; bottom half: increases again.
    spaces_before = abs(middle - i)

    # spaces_between = internal spaces between two '*'
    # Formula:
    # - For rows above the middle, it increases:  -1, 1, 3, 5...
    # - For rows below, it decreases symmetrically.
    # - For i = 0 (top), spaces_between = 0 → only one '*'.
    # - max(0, ...) ensures we never get negative spaces.
    spaces_between = max(0, (i > 0) * (2 * (middle - spaces_before) - 1))

    # First '*' is printed after spaces_before.
    # Second '*' is printed only if spaces_between > 0.
    print(' ' * spaces_before + '*' + ' ' * spaces_between + '*' * (spaces_between > 0))
    


