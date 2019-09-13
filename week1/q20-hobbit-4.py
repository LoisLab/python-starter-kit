'''
Oh wait, the hobbit is starting to learn as he goes...

Questions:
  1. how does this work?
  2. could you program the hobbit to make a mistake, 25% of the time?
'''

def ask_the_hobbit(topic):
  if 'q' in topic.keys():
    response = input(topic['q'] + '? ')
    # if the answer if yes, follow the yes branch -- else follow the no branch
    if response.startswith('y'):
      ask_the_hobbit(topic['y'])
    else:
      ask_the_hobbit(topic['n'])
  else:
    response = input('is it a ' + topic['item'] + '? ')
    if response.startswith('y'):
      # if you and the hobbit agree, he gives you the item
      print('Here, take one of them',topic['item'])
    else:
      # if the hobbit is stumped, he tries to add to the items that he knows about...
      new_item = input('What exactly is this mystery item? ')
      new_q = input('What question would distinguish a ' + new_item + ' from a ' + topic['item'] + '? ')
      topic['q'] = new_q
      topic['y'] = {'item': new_item}
      topic['n'] = {'item': topic.pop('item')}
      # ...and then he starts over
      ask_the_hobbit(everything)

everything = {'item': 'oaken shield'}
ask_the_hobbit(everything)
