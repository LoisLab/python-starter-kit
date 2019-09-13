'''
Playing 20 Questions with a drunken hobbit -- guess the item 
'''

d_and_d = {}
d_and_d['q'] = 'can it hurt somebody? '

d_and_d['y'] = {}
d_and_d['y']['q'] = 'is it pointy, with feathers? '
d_and_d['y']['y'] = {'item':'arrow'}
d_and_d['y']['n'] = {'item':'rock'}

d_and_d['n'] = {}
d_and_d['n']['q'] = 'does it help you do math? '
d_and_d['n']['y'] = {'item':'abacus'}
d_and_d['n']['n'] = {'item':'amulet of health'}


# this is a function, we can use it whenever we want
def ask_the_hobbit(topic):
  if 'q' in topic.keys():
    response = input(topic['q'])
    if response.startswith('y'):
      ask_the_hobbit(topic['y'])
    else:
      ask_the_hobbit(topic['n'])
  else:
    response = input('is it a ' + topic['item'] + '? ')
    if response.startswith('y'):
      print('Here, take one of them',topic['item'])
    else:
      print('Inconceivable!')

  
