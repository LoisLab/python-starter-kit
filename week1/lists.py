'''
takeaway: Python is really good at handling lists
'''

a,b,c = 'elf','halfling','human'
d = ['thief', 'mage', 'tinker']
e = [1,2,3,4,5,6,7,8,9,10]
f = d+e
g = d*2
h = e[3]
i = e[0:3]

'''
one way to add items to a list
'''
j = ['dragon']
j.insert(0,'orc')
j.insert(0,'dire wolf')

'''
one way to remove items from a list
'''
k = ['dragon','orc','dire wolf']
k.pop(0)
k.pop(0)
