__author__ = "Tomasz Rybotycki"

"""
    This script contain methods of computing population mean using median of means
    method in it's original and permutation invariant form. I base on the article
    https://towardsdatascience.com/mean-estimation-median-of-means-6be322ef8d85. 
    
    I assume that random is seeded prior to using these methods.
"""

from numpy import median, mean
from collections.abc import Sequence
from random import shuffle

def mom_mean(population: Sequence[float], elements_per_mean: int) -> float:
    """

        :param elements_per_mean: Number of elements in the sequence from which every
        mean will be estimated.
        :param population: Population of which mean will be estimated.
        :return: Estimator of population mean.
    """
    shuffle(population)

    # Using trick from https://www.geeksforgeeks.org/break-list-chunks-size-n-python/
    elements_blocks = [
        population[i * elements_per_mean:(i + 1) * elements_per_mean]
        for i in range((len(population) + elements_per_mean - 1) // elements_per_mean)
    ]

    means = [mean(block) for block in elements_blocks]

    return median(means)

def prmom_mean(population: Sequence[float], elements_per_mean: int,
               permutations_number: int = 10) -> float:
    """
    :param elements_per_mean: Number of elements in the sequence from which every
    mean will be estimated.
    :param population: Population of which mean will be estimated.
    :param permutations_number:
    :return: Estimator of population mean.
    """
    mom_means = [mom_mean(population, elements_per_mean)]
    return mean(mom_means)
