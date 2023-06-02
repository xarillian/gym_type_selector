import random
import argparse

from const import POKEMON_TYPES


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--l', action='store_true')
    return parser.parse_args()


def validate_input(trainers):
    if trainers == '':
        raise ValueError('You gotta give me some trainers, man.')
    else:
        return [trainer.strip() for trainer in trainers.split(',')]


def assign_types(trainers):
    if len(trainers) > len(POKEMON_TYPES):
        raise ValueError('There are more trainers than Pokemon types.')
    randomized_types = random.sample(POKEMON_TYPES, len(trainers))
    return {trainer: randomized_types[i] for i, trainer in enumerate(trainers)}


def print_trainer_types(trainers, args):
    for trainer, pokemon_type in trainers.items():
        print('{}, the {}-type gym leader!'.format(trainer, pokemon_type))
    if args.l and len(trainers) < len(POKEMON_TYPES):
        remaining_types = [t for t in POKEMON_TYPES if t not in trainers.values()]
        print('\nTypes Remaining: {}'.format(remaining_types))


def main():
    args = parse_args()
    input_trainers = input('Enter trainers (comma separated):\n')
    trainer_list = validate_input(input_trainers)
    trainers_types = assign_types(trainer_list)
    print_trainer_types(trainers_types, args)


main()
