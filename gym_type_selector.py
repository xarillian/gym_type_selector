import random


POKEMON_TYPES = [
  'Normal', 
  'Fire', 
  'Water', 
  'Electric', 
  'Grass', 
  'Ice', 
  'Fighting', 
  'Poison', 
  'Ground',
  'Flying', 
  'Psychic', 
  'Bug', 
  'Rock', 
  'Ghost', 
  'Dragon', 
  'Dark', 
  'Steel', 
  'Fairy'
]


trainers = input('Enter trainers (comma seperated):\n')
if trainers == '':
  raise InputError('You gotta give me some trainers, man.')
else:
  trainers = [trainer.strip() for trainer in trainers.split(',')]
randomized_types = random.sample(POKEMON_TYPES, len(POKEMON_TYPES))

try:
  for trainer in trainers:
    random_type = randomized_types.pop()
    print('{}, the {}-type gym leader!'.format(trainer, random_type))
except IndexError():
  print('No more types to go around!')

if randomized_types:
  print('\nTypes Remaining: {}'.format(randomized_types))
