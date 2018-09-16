import random
from typing import Generator

import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns


def geometric_generator(p: float = 0.5) -> Generator[int, None, None]:
    while True:
        n = 0
        while random.random() > p:
            n += 1
        yield n


def binomial_generator(p: float = 0.5, n: int = 10) -> Generator[int, None, None]:
    while True:
        k = 0
        for i in range(n):
            if random.random() > p:
                k += 1
        yield k


def main():
    sns.set(style='whitegrid')

    n_points = 10000

    fig, axs = plt.subplots(1, 2, sharey=True)

    data = np.fromiter(geometric_generator(), int, count=n_points)
    axs[0].hist(data, bins='auto', label='Geometric distribution')

    data = np.fromiter(binomial_generator(), int, count=n_points)
    axs[1].hist(data, bins='auto', label='Binomial distribution')

    plt.show()


if __name__ == '__main__':
    main()
