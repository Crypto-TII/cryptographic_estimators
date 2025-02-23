# ****************************************************************************
# Copyright 2023 Technology Innovation Institute
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
# ****************************************************************************

import pytest
from ..PKEstimator.pk_algorithm import PKAlgorithm
from ..PKEstimator.pk_problem import PKProblem
from ..base_estimator import BaseEstimator
from math import inf


class PKEstimator(BaseEstimator):
    excluded_algorithms_by_default = []
    def __init__(self, n: int, m: int, q: int, ell: int = 1, memory_bound=inf, **kwargs):
        """Construct an instance of Permuted Kernel Estimator.

        Args:
            n (int): Columns of the matrix.
            m (int): Rows of the matrix.
            q (int): Size of the field.
            ell (int): Rows of the matrix whose permutation should lie in the kernel.
            memory_bound: Memory bound.
            **kwargs: Additional keyword arguments.
                sd_parameters (dict): Optional parameter arguments for SDEstimator used by SBC algorithm.
                cost_for_list_operation: Cost in Fq additions for one list operation in the SBC and KMP algorithm (default n-m).
                memory_for_list_element: Memory in Fq elements for one list element in the SBC and KMP algorithm (default n-m).
                use_parity_row (bool): Enables trick of appending extra (all one) row to the matrix, i.e., m -> m+1 (default: False).
                excluded_algorithms (list or tuple): A list/tuple of excluded algorithms (default: None).
                nsolutions: No. of solutions.
        """
        if not kwargs.get("excluded_algorithms"):
            kwargs["excluded_algorithms"] = []

        kwargs["excluded_algorithms"] += self.excluded_algorithms_by_default
        super(PKEstimator, self).__init__(
            PKAlgorithm, PKProblem(n, m, q, ell=ell, memory_bound=memory_bound, **kwargs), **kwargs)

    def table(self, show_quantum_complexity=0, show_tilde_o_time=0,
              show_all_parameters=0, precision=1, truncate=0):
        """Print table describing the complexity of each algorithm and its optimal parameters.
    
        Args:
            show_quantum_complexity (int): Show quantum time complexity (default: 0)
            show_tilde_o_time (int): Show Ō time complexity (default: 0)
            show_all_parameters (int): Show all optimization parameters (default: 0)
            precision (int): Number of decimal digits output (default: 1)
            truncate (int): Truncate rather than round the output (default: 0)

        Examples:
            >>> from cryptographic_estimators.PKEstimator import PKEstimator
            >>> A = PKEstimator(n=40,m=10,q=7,ell=2)
            >>> A.table()
            +-----------+----------------+
            |           |    estimate    |
            +-----------+-------+--------+
            | algorithm |  time | memory |
            +-----------+-------+--------+
            | KMP       | 146.4 |  105.5 |
            | SBC       | 137.6 |   42.8 |
            +-----------+-------+--------+

        Tests:
            >>> if skip_long_doctests:
            ...     pytest.skip()
            >>> from cryptographic_estimators.PKEstimator import PKEstimator
            >>> A = PKEstimator(n=100,m=50,q=31,ell=2)
            >>> A.table(precision=3, show_all_parameters=1) # long time
            +-----------+------------------------------------------------+
            |           |                    estimate                    |
            +-----------+---------+---------+----------------------------+
            | algorithm |    time |  memory |         parameters         |
            +-----------+---------+---------+----------------------------+
            | KMP       | 243.808 | 243.722 |         {'u': 24}          |
            | SBC       | 241.319 | 236.722 | {'d': 1, 'w': 38, 'w1': 2} |
            +-----------+---------+---------+----------------------------+
        """
        super(PKEstimator, self).table(show_quantum_complexity=show_quantum_complexity,
                                       show_tilde_o_time=show_tilde_o_time,
                                       show_all_parameters=show_all_parameters,
                                       precision=precision, truncate=truncate)
