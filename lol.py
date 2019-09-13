count = 0
lborder = 0
hborder = 100
guess = 50

while True:
    count=count+1
    answer = input('do you have coins more than ' + str(guess) + '?:')
    if answer == 'no':
        hborder = guess
        guess = (lborder + guess + 1 ) // 2
    elif answer == 'yes':
        lborder = guess
        guess = guess = (hborder + guess + 1) // 2
    if count ==6:
        answer = input('do you have coins more than ' + str(guess) + '?:')
        if answer=="yes":
            print("you have"+str(guess+1)+" coins")
        if answer=="no":
            print("you have"+str(guess)+" coins")
            break
print('\nHooray! It took riyas mother', count, 'guess to count coins of riya.', sep=' ')
input('\nPress Enter to Exit.')
