import random

print('What is the magic number (1 to 100) ?')

#a = int(random.random()*100) + 1
num = random.randint(1, 101)
tries = 1
guess = 0

while tries < 7 and guess != num :
    msg = str(tries) +  '>> '
    if (tries == 6):
        msg = str(tries) +  '>> (last chance)'
    guess = int(input(msg))
    if (guess > num):
        print('--> too high')
    elif (guess < num):
        print('--> too low')
    tries += 1

if (guess == num):
    print("Yes! It's", num)
else:
    print('Sorry! My number is', num)
    
