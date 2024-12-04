from math import comb as binomial, inf
from .ranksd_constants import RANKSD_NUMBER_OF_COLUMNS_X_TO_GUESS, \
    RANKSD_LINEAR_VARIABLES_DEGREE, RANKSD_NUMBER_OF_PUNCTURED_POSITIONS


def nb_fqm(m, n, k, r, b):
    """ Returns the number of rows in SMFq^m at bi-degree b,1.

               Args:
                   m (int): Extension degree.
                   n (int): Code length.
                   k (int): Code dimension.
                   r (int): Target rank.
                   b (int): Linear variables degree.
    """
    if (1 > k) or (k > n) or (b < 1) or (r < 1) or (m < 1) or (r > n - k - 1):
        return None

    nn = 0
    for i in range(1, k + 1):
        nn = nn + binomial(n - i, r) * binomial(k + b - 1 - i, b - 1)

    nn = nn - binomial(n - k - 1, r) * binomial(k + b - 1, b)

    return nn


def nb_fq_syz(m, n, k, r, b):
    """ Returns the number of syzygies in SMFq^m at bi-degree b,1.

            Args:
                m (int): Extension degree.
                n (int): Code length.
                k (int): Code dimension.
                r (int): Target rank.
                b (int): Linear variables degree
        """
    if (1 > k) or (k > n) or (b < 1) or (r < 1) or (m < 1) or (r > n - k - 1):
        return None

    nn = 0
    for i in range(1, b + 1):
        nn = nn + (-1) ** (i + 1) * binomial(k + b - i - 1, b - i) * binomial(n - k - 1, r + i)

    return (m - 1) * nn


def compute_nb(m, n, k, r, b):
    """Returns the number of rows.

        Args:
            m (int): Extension degree.
            n (int): Code length.
            k (int): Code dimension.
            r (int): Target rank.
            b (int): Linear variables degree.
    """
    if b == 0:
        if (n - k - 1) >= r:
            return m * binomial(n - k - 1, r)
        else:
            return None

    else:
        nb = nb_fqm(m, n, k, r, b)
        if nb is None:
            return None
        return nb - nb_fq_syz(m, n, k, r, b)


def compute_mb(m, n, k, r, b):
    """Returns the number of columns.

        Args:
            m (int): Extension degree.
            n (int): Code length.
            k (int): Code dimension.
            r (int): Target rank.
            b (int): Linear variables degree
    """
    if (1 > k) or (k > n) or (b < 0) or (r < 1) or (m < 1) or (r > n - k - 1):
        return None

    if b == 0:
        if n >= r:
            return binomial(n, r)
        else:
            return None

    else:
        return binomial(k + b - 1, b) * (binomial(n, r) - m * binomial(n - k - 1, r))


def find_p_sm_fqm(m, n, k, r, b, p_min, p_max):
    """Returns p for the given instance.

       Args:
           m (int): Extension degree.
           n (int): Code length.
           k (int): Code dimension.
           r (int): Target rank.
           b (int): Linear variables degree
           p_min (int): minimum value for p
           p_max (int): maximum value for p
    """
    p = p_min
    nb = compute_nb(m, n - p, k, r, b)
    mb = compute_mb(m, n - p, k, r, b)

    while (nb >= mb - 1) and (n - p > 1) and p <= p_max:
        p = p + 1
        nb = compute_nb(m, n - p, k, r, b)
        mb = compute_mb(m, n - p, k, r, b)

    if nb < mb - 1:
        p = p - 1

    return p


def find_best_choice_param_mm(m, n, k, r, a_min, a_max, p_min, p_max):
    """Returns the best choice (a,p) for Max Minors for the given instance.

         Args:
             m (int): Extension degree.
             n (int): Code length.
             k (int): Code dimension.
             r (int): Target rank.
             a_min (int): minimum value for a
             a_max (int): maximum value for a
             p_min (int): minimum value for p
             p_max (int): maximum value for p
      """
    a = a_min
    nb = compute_nb(m, n - a, k - a, r, 0)
    mb = compute_mb(m, n - a, k - a, r, 0)
    values = {}
    while nb < mb - 1 and a <= a_max:
        a = a + 1
        nb = compute_nb(m, n - a, k - a, r, 0)
        mb = compute_mb(m, n - a, k - a, r, 0)

    if a == k:
        return values

    p = find_p_sm_fqm(m, n - a, k - a, r, 0, p_min, p_max)
    values[RANKSD_NUMBER_OF_COLUMNS_X_TO_GUESS] = a
    values[RANKSD_NUMBER_OF_PUNCTURED_POSITIONS] = p
    return values


def find_b_sm_fqm(m, n, k, r, b_min, b_max):
    """Returns a proper b in range [b_min,b_max] for the given instance.

       Args:
           m (int): Extension degree.
           n (int): Code length.
           k (int): Code dimension.
           r (int): Target rank.
           b_min (int): minimum value for b
           b_max (int): maximum value for b

    """
    b = b_min
    nb = compute_nb(m, n, k, r, b)
    mb = compute_mb(m, n, k, r, b)

    while (nb < mb - 1) and b <= b_max:
        b = b + 1
        nb = compute_nb(m, n, k, r, b)
        mb = compute_mb(m, n, k, r, b)

    if nb >= mb - 1:
        return b
    else:
        return inf


def find_valid_choices_param_sm_fqm(m, n, k, r, a_min, a_max, p_min, p_max, b_min, b_max):
    """Returns valid choices of params (b,a,p) for Support Minors for the given instance.

        Args:
            m (int): Extension degree.
            n (int): Code length.
            k (int): Code dimension.
            r (int): Target rank.
            a_min (int): minimum value for a
            a_max (int): maximum value for a
            p_min (int): minimum value for p
            p_max (int): maximum value for p
            b_min (int): minimum value for b
            b_max (int): maximum value for b
    """
    # This function assumes the system has an unique solution.
    values = find_best_choice_param_mm(m, n, k, r, a_min, a_max, p_min, p_max)
    valid_choices = []
    if len(values) > 0 and values[RANKSD_NUMBER_OF_COLUMNS_X_TO_GUESS] == 0:
        # MM solves it by itself
        return valid_choices

    a0 = values[RANKSD_NUMBER_OF_COLUMNS_X_TO_GUESS]

    for a in range(a0 - 1, -1, -1):
        b = find_b_sm_fqm(m, n - a, k - a, r, b_min, b_max)
        if b == inf:
            break

        p = find_p_sm_fqm(m, n - a, k - a, r, b, p_min, p_max)
        valid_choices.append({RANKSD_LINEAR_VARIABLES_DEGREE: b,
                              RANKSD_NUMBER_OF_COLUMNS_X_TO_GUESS: a,
                              RANKSD_NUMBER_OF_PUNCTURED_POSITIONS: p})

    return valid_choices
