def cheese_and_cracker(cheese_count,box_of_cracker):
    print(' if you have {} cheese'.format(cheese_count))
    print('you have {} boxes of crackers'.format(box_of_cracker))
    print(' man that is enough for party')
    print(' get a blanket \n')


print('we can just give the function numbers directly:')
cheese_and_cracker(20,30)

print ('we can use variable from our script:')
amount_of_cheese=10
amount_of_cracker=50

cheese_and_cracker(amount_of_cheese,amount_of_cracker)

print('we can enven do math inside too:')
cheese_and_cracker(10+20,5+6)


