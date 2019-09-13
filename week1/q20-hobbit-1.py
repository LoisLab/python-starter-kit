'''
Playing 20 Questions with a drunken hobbit -- guess the item
'''

'''
to begin, the hobbit only knows 1 thing
'''
d_and_d = {'item': 'amulet of health'}

print('Answer my questions and I will give you an item...')

response = input('is it a ' + d_and_d['item'] + '? ')

if response.startswith('n'):
    print('Inconceivable!')
else:
    print('Take this here', d_and_d['item'])
