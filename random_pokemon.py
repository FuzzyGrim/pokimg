import random
import os
import sys

def get_roman_nums(generation):
    roman = {
        1: "I",
        2: "II",
        3: "III",
        4: "IV",
        5: "V",
        6: "VI",
        7: "VII",
        8: "VIII",
    }

    return roman[generation]

def get_index(generation):
    ranges = {
        1: (1, 151),
        2: (152, 251),
        3: (252, 386),
        4: (387, 493),
        5: (494, 649),
        6: (650, 721),
        7: (722, 809),
        8: (810, 898),
    }
    start, stop = ranges[generation]
    
    return random.randint(start, stop)

def get_generation():
    generation = random.randint(1, 8)
    if len(sys.argv) > 1:        
        generations = sys.argv[2:]

        if generations:
            if "-" in generations[0]:
                interval = generations[0].split("-")
                generations = list(range(int(interval[0]), int(interval[1]) + 1))

            if not all(map(lambda g: 1 <= int(g) <= 8, generations)):
                raise ValueError("Invalid generation, it must be from 1-8.")
        
            generation = int(random.choice(generations))

    return generation

def main():
    absolute_path = os.path.dirname(__file__)

    generation = get_generation()
    index = get_index(generation)

    with open(f'{absolute_path}/namelist.txt') as file:
        pokemons = file.read().splitlines()
        pokemon = pokemons[index - 1]
        print(f"{pokemon} - {get_roman_nums(generation)} Generation")

if __name__ == "__main__":
    main()