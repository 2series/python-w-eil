number = 10
guess = 14

if guess > number:
    print('HIGH')
elif guess < number :
    print('LOW')
else:
    print('Correct')


if guess > number or guess < number:
    print('Guess is wrong')
else:
    print('Guess is Correct')