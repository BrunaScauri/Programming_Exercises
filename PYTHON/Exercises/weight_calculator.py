# WEIGHT EXERCISE
weight = int(input('Weight: '))
measure = input('(K)g or (L)bs: ')

if measure == 'k':
    result = int(weight * 0.45)
    print('Weight in Kg: ', result)
elif measure == 'l':
    result = int(weight / 0.45)
    print('Weight in lbs: ', result)
