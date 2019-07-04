print(''''
you enter a dark room with two doors.
do you go through door #1 or door #2?
''')
door=input('>')

if door==1:
    print('there is a giat bear here eating a cheese cake')
    print('what do you do')
    print('1.take the cake')
    print('2.scream at the bear')

    bear=input('>')
    if bear=='1':
        print('the bear take your face off. good job')
    elif bear=='2':
        print('the bear eats your legs off .good jod')
    else:
        print(format,'well,doing{bear} ia probably better')
        print('bear run away')
elif door=='2':
    print('you stare into the endless abyss at cthulhu\'s retina')
    print('1.blueberries')
    print('2.yellow jackett clotjespins')
    print('3.understanding revolvers yelling melodies')

    insanity=input('>')
    if insanity=='1'or'2':
        print('your body survives powered by a mind of jello')
        print('good jod')
    else:
        print('the insanity rots your eyes into a pool of muck')
        print('good job')
else:
    print('you stumble aroiund and fall on a knife and die. good job')