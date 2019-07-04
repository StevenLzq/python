people=30
cars=40
trucks=15

if cars>people:
    print('we should take the cars')
elif cars<people:
    print('we should not take the cars')
else:
    print('we can not decide')

if trucks>cars:
    print('there are too many trucks')
elif trucks<cars:
    print('maybe we could take the trucks')
else:
    print('we still can not decide')

if people>trucks:
    print('alright,let us take the trucks')
else:
    print('fine let us stay home then')