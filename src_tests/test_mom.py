__author__ = "Tomasz Rybotycki"

"""
    This script contains median of means estimator tests.
"""

from unittest import TestCase
from ..src.MOM.median_of_means import mom_mean, pimom_mean
from numpy import mean
from numpy.random import choice, standard_t

class MOMTests(TestCase):

    def __init__(self, *args, **kwargs):
        super(MOMTests, self).__init__(*args, **kwargs)
        self._population = standard_t(df=1, size=1000)
        self._sample = choice(self._population, size=100)

    def test_mom_accuracy_on_students_distribution(self):
        population_mean = mean(self._population)
        sample_mean = mean(self._sample)
        sample_mom_mean = mom_mean(self._sample, 10)
        sample_mean_error_sq = ((population_mean - sample_mean)**2)
        sample_mom_mean_error_sq = ((population_mean - sample_mom_mean)**2)
        self.assertGreaterEqual(sample_mean_error_sq, sample_mom_mean_error_sq)

    def test_mom_accuracy_on_students_distribution(self):
        population_mean = mean(self._population)
        sample_mean = mean(self._sample)
        sample_pimom_mean = pimom_mean(self._sample, 10)
        sample_mean_error_sq = ((population_mean - sample_mean) ** 2)
        sample_pimom_mean_error_sq = ((population_mean - sample_pimom_mean) ** 2)
        self.assertGreaterEqual(sample_mean_error_sq, sample_pimom_mean_error_sq)
