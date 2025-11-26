# game Guess the second multiple game
print('Guess the second multiple game')
# import random library
import random
# use random library with randint
rnd = random.randint(1,10)
num = input('inter the num: ')
# Convert the number to a string
num_str = str(num)
# Reverse the string
reversed_str= num_str[::-1]
 # Convert the reversed string back to an integer
reversed_num = int(reversed_str)

print(reversed_num)

zarb2num = reversed_num * rnd

print(zarb2num)

hads = int(input('inter your guess: '))

if hads == rnd:
    print('good!!')

else:
    print('try agin!!')
