from ..MQEstimator.series.nmonomial import NMonomialSeries
from math import log2
from sage.arith.misc import is_prime_power
from sage.functions.other import binomial


def ngates(q, n, theta=2):
    """
    Return the number of gates for the given number of multiplications in a finite field

    INPUT:

    - ``q`` -- order of the finite field
    - ``n`` -- no. of multiplications (logarithmic)
    - ``theta`` -- exponent of the conversion factor

    EXAMPLES::

        sage: from cryptographic_estimators.MQEstimator.mq_helper import ngates
        sage: ngates(16, 16)
        20.0

    TESTS::

        sage: ngates(6, 2**16)
        Traceback (most recent call last):
        ...
        ValueError: q must be a prime power
    """
    if not is_prime_power(q):
        raise ValueError("q must be a prime power")
    if theta:
        return n + log2(log2(q)) * theta
    else:
        return n + log2(2 * log2(q) ** 2 + log2(q))


def nmonomials_of_degree(d, n, q):
    """
    Return the number of `n`-variables monomials of degree `d`

    .. NOTE::

        If `q` is provided, then it considers the monomials in a ring modulo the ideal generated by the field equations

    INPUT:

    - ``d`` -- degree
    - ``n`` -- no. of variables
    - ``q`` -- order of finite field

    EXAMPLES::

        sage: from cryptographic_estimators.MQEstimator.mq_helper import nmonomials_of_degree
        sage: nmonomials_of_degree(d=2, n=10, q=2)
        45
    """
    series = NMonomialSeries(n, q, max_prec=d+1)
    return series.nmonomials_of_degree(d)


def nmonomials_up_to_degree(d, n, q):
    """
    Return the number of `n`-variables monomials up to degree `d`

    .. NOTE::

        If `q` is provided, then it considers the monomials in a ring modulo the ideal generated by the field equations

    INPUT:

    - ``d`` -- degree
    - ``n`` -- no. of variables
    - ``q`` -- order of finite field

    EXAMPLES::

        sage: from cryptographic_estimators.MQEstimator.mq_helper import nmonomials_up_to_degree
        sage: nmonomials_up_to_degree(d=2, n=10, q=2)
        56
    """
    series = NMonomialSeries(n, q, max_prec=d+1)
    return series.nmonomials_up_to_degree(d)


def sum_of_binomial_coefficients(n, l):
    r"""
    Return the `\sum_{j=0}^{l} \binom{n}{j}`

    INPUT:

    - ``n`` -- a non-negative integer
    - ``l`` -- a non-negative integer

    EXAMPLES::

        sage: from cryptographic_estimators.MQEstimator.mq_helper import sum_of_binomial_coefficients
        sage: sum_of_binomial_coefficients(5, 2)
        16
    """
    if l < 0:
        raise ValueError('l must be a non-negative integer')
    return sum(binomial(n, j) for j in range(l + 1))