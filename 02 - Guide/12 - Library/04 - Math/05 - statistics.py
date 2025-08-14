"""
Statistics

* The statistics module provides functions for calculating mathematical
  statistics of numeric (Real-valued) data
* These functions can be used to calculate averages, measures of central
  location, measures of spread, and measures of shape
* The avilable functions support int, float, Decimal and Fraction data types
* The module is divided into three categories:
  * Averages and Measures of Central Location
  * Measures of Variability or Spread
  * Statistics for Relations Between Two Inputs
* The term kernel is used in statistical analysis to refer to a window function
* The available kernel functions are: normal/gauss, logistic, sigmoid,
  rectangular/uniform, triangular, parabolic/epanechnikov, quartic/biweight,
  triweight, cosine
* Below there a glossary of the terms found on the statistics module
###############################################################################
Term        Description
###############################################################################
kernel      A window function used in statistical analysis
kde         Kernel Density Estimation
h           The bandwidth of a kernel density estimate
mu          The arithmetic mean of a data set
sigma       The standard deviation of a data set
xbar/ybar   The mean of a sample to avoid recalculation
###############################################################################
"""


###############################################################################
# Module Import
###############################################################################


# Importing the module
# * We can import this module using the `import` statement as follows
import statistics


###############################################################################
# Calculating Averages
###############################################################################


# mean(data)
# * The `mean()` function calculates the arithmetic mean of a sequence of data
# * If data is empty, StatisticsError is raised
# * The arithmetic mean is the sum of the data divided by the number of data
#   points
x = 1, 2, 3
y = statistics.mean(x)
print(y)
# 2.0


# fmean(data, weights=None)
# * The `fmean()` function calculates the arithmetic mean of a sequence of data
# * The difference between `mean()` and `fmean()` is that `fmean()` converts
#   data to floats before calculating the mean
# * The `weights` argument can be used to determine the weight of each value in
#   the data
x = 1, 2, 3
y = statistics.fmean(x)
print(y)
# 2.0


# geometric_mean(data)
# * The `geometric_mean()` function calculates the geometric mean of a sequence
#   of data
# * The geometric mean is the nth root of the product of the data, where n is
#   the number of data points
x = 1, 2, 3
y = statistics.geometric_mean(x)
print(y)
# 1.8171205928321397


# harmonic_mean(data, weights=None)
# * The `harmonic_mean()` function calculates the harmonic mean of a sequence
#   of data
# * The harmonic mean is the reciprocal of the arithmetic mean of the
#   reciprocals of the data
# * The `weights` argument can be used to determine the weight of each value in
#   the data
x = 1, 2, 3
y = statistics.harmonic_mean(x)
print(y)
# 1.6363636363636365


# kde(data, h, kernel='normal', *, cumulative=False)
# * KDA means Kernel Density Estimation
# * The `kde()` function creates a continuous probability density function or
#   cumulative distribution function from discrete samples
# * The basic idea is to smooth the data using a kernel function. to help draw
#   inferences about a population from a sample
# * The degree of smoothing is controlled by the scaling parameter h which is
#   called the bandwidth
# * The kernel function can be specified using the `kernel` argument. The
#   default is 'normal' which uses the normal distribution
# * The `cumulative` argument can be set to True to return the cumulative
#   distribution function
# * The function returns a callable object that can be used to evaluate the
#   density or cumulative distribution at any point
x = 1, 2, 3
fn = statistics.kde(x, 1.5, 'sigmoid', cumulative=True)
y = fn(1.5)
print(y)
# 0.408139004776195


# kde_random(data, h, kernel='normal', *, seed=None)
# * The `kde_random()` function returns Return a function that makes a random
#   selection from the estimated probability density function produced by
#   `kde(data, h, kernel)`
# * The `seed` argument can be used to allow reproducible selections
# * Note that the function returned will use random numbers and does not accept
#   any arguments
x = 1, 2, 3
fn = statistics.kde_random(x, 1.5, 'sigmoid', seed=15)
y = fn()
print(y)
# -5.000527772335774


# median(data)
# * The `median()` function calculates the median of a sequence of data
# * The median is the middle value of the data when it is sorted
# * If the data has an odd number of values, the median is the middle value
# * If the data has an even number of values, the median is the average of the
#   two middle values
# * Note that in the example below, both values (3 and 5) are in the middle of
#   the data, and the average was calculated
x = 1, 3, 5, 7
y = statistics.median(x)
print(y)
# 4.0


# median_low(data)
# * Similar to the `median()` function, but it returns the low value if the
#   number of values is even
x = 1, 3, 5, 7
y = statistics.median_low(x)
print(y)
# 3


# median_high(data)
# * Similar to the `median()` function, but it returns the high value if the
#   number of values is even
x = 1, 3, 5, 7
y = statistics.median_high(x)
print(y)
# 5


# median_grouped(data, interval=1.0)
# * The `median_grouped()` function calculates the median of grouped continuous
#   data
# * The median is calculated as the 50th percentile using interpolation
# * The `interval` argument can be used to specify the interval of the data
x = 1, 3, 5, 7
y = statistics.median_grouped(x)
print(y)
# 4.5


# mode(data)
# * The `mode()` function calculates the mode of a sequence of data
# * The mode is the value that appears most frequently in the data
# * If there are multiple modes with the same frequency, the first one
#   encountered in the data is returned
x = 1, 2, 2, 3, 3
y = statistics.mode(x)
print(y)
# 2


# multimode(data)
# * Similar to the `mode()` function, but it returns a list of the most
#   frequently occurring values in the order they were first encountered in the
#   data
x = 1, 2, 2, 3, 3
y = statistics.multimode(x)
print(y)
# [2, 3]


# quantiles(data, *, n=4, method='exclusive')
# * The `quantiles()` function divides data into n continuous intervals with
#   equal probability
# * Returns a list of n - 1 cut points separating the intervals
# * Set n to 4 for quartiles (the default). Set n to 10 for deciles. Set n to
#   100 for percentiles which gives the 99 cuts points that separate data into
#   100 equal sized groups
# * The `method` argument can be set to 'inclusive' to include the endpoints of
#   the intervals
x = 1, 2, 3, 4, 5
y = statistics.quantiles(x, method='inclusive')
print(y)
# [2.0, 3.0, 4.0]


###############################################################################
# Calculating Variability or Spread
###############################################################################


# pvariance(data, mu=None)
# * The `pvariance()` function calculates the population variance of a sequence
#   of data
# * If the optional second argument `mu` is given, it is typically the mean of
#   the data. It can also be used to compute the second moment around a point
#   that is not the mean. If it is missing or None (the default), the
#   arithmetic mean is automatically calculated
# * Use this function to calculate the variance from the entire population. To
#   estimate the variance from a sample, the variance() function is usually a
#   better choice
x = 1, 2, 3
y = statistics.pvariance(x)
print(y)
# 0.6666666666666666


# variance(data, xbar=None)
# * The `variance()` function calculates the sample variance of a sequence of
#   data
# * The `xbar` argument can be used to specify the mean of the data. If it is
#   missing or None (the default), the arithmetic mean is automatically
#   calculated
x = 1, 2, 3
y = statistics.variance(x)
print(y)
# 1.0


# pstdev(data, mu=None)
# * The `pstdev()` function calculates the population standard deviation of a
#   sequence of data
# * The `mu` argument can be used to specify the mean of the data. If it is
#   missing or None (the default), the arithmetic mean is automatically
x = 1, 2, 3
y = statistics.pstdev(x)
print(y)
# 0.816496580927726


# stdev(data, xbar=None)
# * The `stdev()` function calculates the sample standard deviation of a
#   sequence
# * The `xbar` argument can be used to specify the mean of the data. If it is
#   missing or None (the default), the arithmetic mean is automatically
x = 1, 2, 3
y = statistics.stdev(x)
print(y)
# 1.0


###############################################################################
# Statistics for Relations Between Two Inputs
###############################################################################


# covariance(x, y, /)
# * The `covariance()` function returns the sample covariance of two inputs x
#   and y. Covariance is a measure of the joint variability of two inputs
x = 1, 2, 3
y = 2, 3, 4
z = statistics.covariance(x, y)
print(z)
# 1.0


# correlation(x, y, /, *, method='linear')
# * The `correlation()` function calculates the correlation between two
#   sequences of data
# * The correlation is a value between -1 and 1 that indicates the strength and
#   direction of a linear relationship between two variables
# * A correlation of 1 indicates a perfect positive linear relationship, a
#   correlation of -1 indicates a perfect negative linear relationship, and a
#   correlation of 0 indicates no linear relationship
# * The `method` argument can be set to 'linear' or 'ranked' to specify the
#   method used to calculate the correlation
x = 1, 2, 3
y = 2, 3, 4
z = statistics.correlation(x, y)
print(z)
# 1.0


# linear_regression(x, y, /, *, proportional=False)
# * The `linear_regression()` function calculates the slope, intercept, and
#   correlation coefficient of a linear regression between two sequences of
#   data
# * The function returns an LinearRegression object that contains the slope and
#   intercept values
# * The `proportional` argument can be used to the define that the independent
#   variable x and the dependent variable y are assumed to be directly
#   proportional
# * Note that this function is the core for Artificial Intelligence and Machine
#   Learning algorithms
x = 1, 1, 2
y = 2, 3, 4
z = statistics.linear_regression(x, y)
print(z.slope, z.intercept)
# 1.5 1.0


###############################################################################
# NormDist Class
###############################################################################


# Creating a NormalDist object
# * NormalDist is a tool for creating and manipulating normal distributions of
#   a random variable. It is a class that treats the mean and standard
#   deviation of data measurements as a single entity
# * The constructor takes two arguments: `mu` and `sigma`
# * The `mu` argument represents the arithmetic mean and `sigma` represents the
#   standard deviation
# * Below is an example of how to create a NormalDist object
x = statistics.NormalDist(0.5, 0.5)


###############################################################################
# NormDist Class Methods
###############################################################################


# from_samples(data, *, mu=None, sigma=None)
# * The `from_samples()` method creates a NormalDist object from a sample of
#   data
x = 1, 2, 3
y = statistics.NormalDist.from_samples(x)
print(y)
# NormalDist(mu=2.0, sigma=0.816496580927726)


###############################################################################
# NormDist Properties
###############################################################################


# mean
# * The `mean` property returns the mean of the NormalDist object
x = statistics.NormalDist(0.4, 0.15)
y = x.mean
print(y)
# 0.4


# median
# * The `median` property returns the median of the NormalDist object
x = statistics.NormalDist(0.4, 0.15)
y = x.median
print(y)
# 0.4


# mode
# * The `mode` property returns the mode of the NormalDist object
x = statistics.NormalDist(0.4, 0.15)
y = x.mode
print(y)
# 0.4


# stdev
# * The `stdev` property returns the standard deviation of the NormalDist
#   object
x = statistics.NormalDist(0.4, 0.15)
y = x.stdev
print(y)
# 0.15


# variance
# * The `variance` property returns the variance of the NormalDist object
x = statistics.NormalDist(0.4, 0.15)
y = x.variance
print(y)
# 0.0225


###############################################################################
# NormDist Methods
###############################################################################


# samples(n, *, seed=None)
# * The `samples()` method returns a generator that produces n random samples
#   from the NormalDist object
# * Returns a list of float values
# * The `seed` argument can be used to allow reproducible selections
x = statistics.NormalDist(0.4, 0.15)
y = x.samples(5, seed=15)
print(list(y))
# [0.548, 0.401, 0.401, 0.401, 0.401]


# pdf(x)
# * The `pdf()` method returns the probability density function of the
#   NormalDist
x = statistics.NormalDist(0.4, 0.15)
y = x.pdf(0.5)
print(y)
# 2.666666666666666


# cdf(x)
# * The `cdf()` method returns the cumulative distribution function of the
#   NormalDist
x = statistics.NormalDist(0.4, 0.15)
y = x.cdf(0.5)
print(y)
# 0.5


# inv_cdf(p)
# * The `inv_cdf()` method returns the inverse cumulative distribution function
#   of the NormalDist
x = statistics.NormalDist(0.4, 0.15)
y = x.inv_cdf(0.5)
print(y)
# 0.4


# overlap(other)
# * The `overlap()` method returns the overlap of two NormalDist objects
x = statistics.NormalDist(0.4, 0.15)
y = statistics.NormalDist(0.5, 0.15)
z = x.overlap(y)
print(z)
# 0.7388826803635273


# quantiles(n=4)
# * The `quantiles()` method returns the quantiles of the NormalDist object
# * The `n` argument can be set to 4 for quartiles (the default), 10 for
#   deciles, or 100 for percentiles
x = statistics.NormalDist(0.4, 0.15)
y = x.quantiles()
print(y)
# [0.29882653747058774, 0.4, 0.5011734625294123]


# zscore(x)
# * The `zscore()` method returns the z-score of a value x in the NormalDist
#   object
x = statistics.NormalDist(0.4, 0.15)
y = x.zscore(0.5)
print(y)
# 0.6666666666666665
