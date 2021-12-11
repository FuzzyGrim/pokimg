import random
import os

absolute_path = os.path.dirname(__file__)

def main():
    with open(f'{absolute_path}/namelist.txt') as file:
        lines = file.read().splitlines()
        print(random.choice(lines))

if __name__ == "__main__":
    main()