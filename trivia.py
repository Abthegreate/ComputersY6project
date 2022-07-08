print('Hello, welcome to trivia!')
print('All answers lowercase!')
ans = input('Are you ready to play(yes/no): ')
score = 0
total_q = 4


if ans.lower() == 'yes':
    ans = input('1. When was python invented? ')
    if ans.lower() == '1991':
        score += 1
        print('Correct')
    else:
        print('Incorrect')

    ans = input ( '2. Who is the founder of python?' )
    if ans.lower ( ) == 'guido van rossum':
        score += 1
        print ( 'Correct' )
    else:
        print ( 'Incorrect' )

    ans = input ( '3. How many people downloaded python?' )
    if ans.lower ( ) == '34.5 million' or ans.lower == '34.5':
        score += 1
        print ( 'Correct' )
    else:
        print ( 'Incorrect' )

    ans = input ( '4.How much market share does python own ?' )
    if ans.lower ( ) == '48.07%':
        score += 1
        print ( 'Correct' )
    else:
        print ( 'Incorrect' )
print('Thank you for playing!')
print('You got', score,'questions correct')
mark = (score/total_q) * 100
print('Mark: ',mark,'%')
print('Goodbye, thanks for doing the quiz!')






