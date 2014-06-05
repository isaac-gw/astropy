# Licensed under a 3-clause BSD style license - see LICENSE.rst

"""
This module provides utility functions for the models package
"""

from __future__ import (absolute_import, unicode_literals, division,
                        print_function)

import numpy as np

from ..extern.six.moves import xrange, zip

__all__ = ['can_broadcast', 'poly_map_domain', 'comb']



def can_broadcast(shape_a, shape_b):
    """
    Determines whether two Numpy arrays can be broadcast with each other
    based on their shape tuple alone.

    Parameters
    ----------
    shape_a : tuple
        The shape tuple of the first array.
    shape_b : tuple
        The shape tuple of the second array.

    Returns
    -------
    can_broadcast : bool
        `True` if two arrays with the given shapes can be broadcast against
        each other.
    """

    for dim_a, dim_b in zip(reversed(shape_a), reversed(shape_b)):
        if not (dim_a == 1 or dim_b == 1 or dim_a == dim_b):
            return False

    return True


def poly_map_domain(oldx, domain, window):
    """
    Map domain into window by shifting and scaling.

    Parameters
    ----------
    oldx : array
          original coordinates
    domain : list or tuple of length 2
          function domain
    window : list or tuple of length 2
          range into which to map the domain
    """
    domain = np.array(domain, dtype=np.float64)
    window = np.array(window, dtype=np.float64)
    scl = (window[1] - window[0]) / (domain[1] - domain[0])
    off = (window[0] * domain[1] - window[1] * domain[0]) / (domain[1] - domain[0])
    return off + scl * oldx


def comb(N, k):
    """
    The number of combinations of N things taken k at a time.

    Parameters
    ----------
    N : int, array
        Number of things.
    k : int, array
        Number of elements taken.

    """
    if (k > N) or (N < 0) or (k < 0):
        return 0
    val = 1
    for j in xrange(min(k, N - k)):
        val = (val * (N - j)) / (j + 1)
    return val


def array_repr_oneline(array):
    """
    Represents a multi-dimensional Numpy array flattened onto a single line.
    """

    r = np.array2string(array, separator=',', suppress_small=True)
    return ' '.join(l.strip() for l in r.splitlines())
