'''
Playing 20 Questions with a drunken hobbit -- guess the item
'''

d_and_d = {}
d_and_d['q'] = 'is it pointy, with feathers'
d_and_d['y'] = {'item':'arrow'}
d_and_d['n'] = {'item':'amulet of health'}


print('Answer my questions and I will give you an item...')

# the question is under the key 'q' in the dictionary
response = input(d_and_d['q'] + '? ')

# depending on the response, guess the 'yes' item or the 'no' item
if response.startswith('y'):
    response = input('is it a ' + d_and_d['y']['item'] + '? ')
else:
    response = input('is it a ' + d_and_d['n']['item'] + '? ')

if response.startswith('n'):
    print('Inconceivable!')
else:
    print('Take one of them whatever it was...')
