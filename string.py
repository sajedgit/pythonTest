player = 'Thomas'
points = 33
k=" Last night, "+player+" scored "+str(points)+" points. "
print(f'Last night, {player} scored {points} points.')  # concatenation

a,b,c=3,4.7,'\nsajed\n'

print("I'm going to inject %s here by %d to %s." %(a,b,c))

print(repr(player))


print('Floating point numbers: %2.1f' %(2.175909))

print('may name is %s and my age is %d \n my weight is %2.5f thanks for you info %r' %('sajed',32,73.52,'bye bye!!!'))


s="my name is {l} and my age is {l}";
print(s.format(l='sajed'))


print('{0:7} | {1:40}'.format('Fruit', '40'))
print('{0:7} | {1:9}'.format('Apples', 'hghg'))
print('{0:1} | {1:9}'.format('Oranges', 10))