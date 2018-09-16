import random
from typing import Generator

import numpy as np


def hit_generator(p: float = 0.5) -> Generator[bool, None, None]:
    while True:
        yield (random.random() > p) or (random.random() > p)


def main():
    for n_points in [1000, 10000, 100000, 1000000]:
        print(f'n_points={n_points}')
        data = np.fromiter(hit_generator(), bool, n_points)
        print(f'{data.mean()}')


if __name__ == '__main__':
    main()
