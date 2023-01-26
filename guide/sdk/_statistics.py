"""
Statistics module

* This module provides functions for calculating mathematical statistics of
  numeric (Real-valued) data.
* Unless explicitly noted, these functions support int, float, Decimal and
  Fraction
* Reference: https://docs.python.org/3/library/statistics.html
"""
import statistics


###############################################################################
# Averages and measures of central location
# * These functions calculate an average or typical value from a population or
#   sample
###############################################################################


# mean(data)
# * Return the sample arithmetic mean ("average") of data which can be a
#   sequence or iterable
lst = [1, 2, 3, 4]
print(statistics.mean(lst))
# 2.5


# fmean(data)
# * Convert data to floats and compute the arithmetic mean
# * This runs faster than the mean() function and it always returns a float
lst = [1, 2, 3]
print(statistics.fmean(lst))
# 2.0


# geometric_mean(data)
# * Convert data to floats and compute the geometric mean
# * The geometric mean indicates the central tendency or typical value of the
#   data using the product of the values
lst = [1, 2, 3]
print(statistics.geometric_mean(lst))
# 1.8171205928321397


# harmonic_mean(data)
# * Return the harmonic mean of data, a sequence or iterable of real-valued
#   numbers
# * The harmonic mean of three values a, b and c will be equivalent to
#   3/(1/a + 1/b + 1/c)
lst = [1, 2, 3]
print(statistics.harmonic_mean(lst))
# 1.6363636363636365


# median(data)
# * Return the median (middle value) of numeric data, using the common 'mean of
#   middle two' method
# * If data is empty, StatisticsError is raised
# * data can be a sequence or iterable
lst = [1, 3, 5, 7]
print(statistics.median(lst))
# 4.0


# median_low(data)
# * Return the low median of numeric data
# * If data is empty, StatisticsError is raised
# * data can be a sequence or iterable
lst = [1, 3, 5, 7]
print(statistics.median_low(lst))
# 3


# median_high(data)
# * Return the high median of data
# * If data is empty, StatisticsError is raised
# * data can be a sequence or iterable
lst = [1, 3, 5, 7]
print(statistics.median_high(lst))
# 5


# median_grouped(data, interval=1)
# * Return the median of grouped continuous data, calculated as the 50th
#   percentile, using interpolation
# * If data is empty, StatisticsError is raised
# * data can be a sequence or iterable
lst = [1, 3, 5, 7]
print(statistics.median_grouped(lst))
# 4.5


# mode(data)
# * Return the single most common data point from discrete or nominal data.
# * The mode (when it exists) is the most typical value and serves as a measure
#   of central location
# * If there are multiple modes with the same frequency, returns the first one
#   encountered in the data
lst = [1, 1, 2, 3, 3, 3, 3, 4]
print(statistics.mode(lst))
# 3


# multimode(data)
# * Return a list of the most frequently occurring values in the order they
#   were first encountered in the data.
# * Will return more than one result if there are multiple modes or an empty
#   list if the data is empty
lst = [1, 1, 2, 3, 3, 3, 4, 5, 5, 5, 6]
print(statistics.multimode(lst))
# [3, 5]


# quantiles(data, *, n=4, method='exclusive')
# * Divide data into n continuous intervals with equal probability.
# * Returns a list of n - 1 cut points separating the intervals.
# * Set n to 4 for quartiles (the default). Set n to 10 for deciles. Set n to
#   100 for percentiles which gives the 99 cuts points that separate data into
#   100 equal sized groups. Raises StatisticsError if n is not least 1.
lst = [2.75, 1.75, 1.25, 0.25, 0.5, 1.25, 3.5]
print(statistics.quantiles(lst))
# [0.5, 1.25, 2.75]


###############################################################################
# Measures of spread
# * These functions calculate a measure of how much the population or sample
#   tends to deviate from the typical or average values
###############################################################################


# pstdev(data, mu=None)
# * Return the population standard deviation (the square root of the population
#   variance)
# * See pvariance() for arguments and other details
lst = [1.5, 2.5, 2.5, 2.75, 3.25, 4.75]
print(statistics.pstdev(lst))
# 0.986893273527251


# pvariance(data, mu=None)
# * Return the population variance of data, a non-empty sequence or iterable of
#   real-valued numbers
# * Variance, or second moment about the mean, is a measure of the variability
#   (spread or dispersion) of data. A large variance indicates that the data is
#   spread out; a small variance indicates it is clustered closely around the
#   mean
# * If the optional second argument mu is given, it is typically the mean of
#   the data. It can also be used to compute the second moment around a point
#   that is not the mean. If it is missing or None (the default), the
#   arithmetic mean is automatically calculated
lst = [0.0, 0.25, 0.25, 1.25, 1.5, 1.75, 2.75, 3.25]
print(statistics.pvariance(lst))
# 1.25


# stdev(data, xbar=None)
# * Return the sample standard deviation (the square root of the sample
#   variance)
# * See variance() for arguments and other details
lst = [1.5, 2.5, 2.5, 2.75, 3.25, 4.75]
print(statistics.stdev(lst))
# 1.0810874155219827


# variance(data, xbar=None)
# * Return the sample variance of data, an iterable of at least two real-valued
#   numbers
# * Variance, or second moment about the mean, is a measure of the variability
#   (spread or dispersion) of data. A large variance indicates that the data is
#   spread out; a small variance indicates it is clustered closely around the
#   mean
# * If the optional second argument xbar is given, it should be the mean of
#   data. If it is missing or None (the default), the mean is automatically
#   calculated
lst = [2.75, 1.75, 1.25, 0.25, 0.5, 1.25, 3.5]
print(statistics.variance(lst))
# 1.3720238095238095
