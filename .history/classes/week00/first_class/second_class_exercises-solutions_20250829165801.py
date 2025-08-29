
#1  print 'hello' 5 times using an arithmetic operator

print('Hello' * 5)

#2 print 'hello' 5 times using a loop

for i in range(5):
    print('Hello')


# print 'hello' 5 times on the same line using a loop

for i in range(5):
    print('Hello', end = ' - ')

''' using nested loops print the following:

00 01 02
10 11 12
20 21 22

'''

for i in range(3):
    for j in range(3):
        print(str(i) + str(j), end = ' ')
    print()

print('\n')

for i in range(3):
    for j in range(3):
        print(i , end ='')
        print(j, end = ' ')
    print()
print('\n')


# define txt and input some text from the keyboard into it

txt =input('enter some text: ')

# print each letter in txt 

for l in txt:
    print(l)

# assign the variable letter to the first letter in txt

letter = txt[0]

# print out all the letters in txt that are equal to the first letter

'''
say txt = 'the cat in the hat was read today'
't' is the first letter

result: tttt
'''

for l in txt:
    if l == letter:
        print(l, end='')


'''
# suppose we had a list of n elements. create a new list that
  shifts the elements by 3

    myList = ['apple', 'orange', 'pear', 'blueberry', 'peach']
      shifted_list = ['pear', 'blueberry', 'peach', 'apple', 'orange']

        Hints:
            1) use len(), %, enumerate
            2) also assign shifted_list = [None] * length  (you'll need to determine 
                the length variable)
            3) shift inside the for loop
            4) print out the printed list outside the for loop
'''

myList = ['apple', 'orange', 'pear', 'blueberry', 'peach']
length = len(myList)
shifted_list = [None] * length

shift = 3

for idx, item in enumerate(myList):
    new_idx = (idx + shift) % length
    shifted_list[new_idx] = item

print(myList)
print(shifted_list)



'''
Concepts covered, tools for your toolchest

Arithmetic operators on strings (*)
Loops (for, nested loops)
Controlling print output (end)
String indexing and iteration
Conditionals
List manipulation and modular arithmetic
Using len() and enumerate()

'''
