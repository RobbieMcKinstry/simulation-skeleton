from numpy.random import normal, uniform

def normal_var(center, std):
    """
    Center is the center of the normal curve
    Std is the standard deviation
    Taken from http://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.norm.html
    """
    return normal(center, std)


def uniform_var(low, high):
'''
Low: the lower bound
High: the upper bound
Includes low but excludes high
Taken from http://docs.scipy.org/doc/numpy-1.10.0/reference/generated/numpy.random.uniform.html
'''
    return uniform(low, high)

