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


from .if_algorithm import IFAlgorithm
from .if_problem import IFProblem
from ..base_estimator import BaseEstimator
from math import inf


class IFEstimator(BaseEstimator):
    """
    Construct an instance of IFEstimator

    INPUT:

    - ``excluded_algorithm`` -- A list/tuple of excluded algorithms (default: None)

    """
    excluded_algorithms_by_default = []

    def __init__(self, n:int, memory_bound=inf, **kwargs): # Fill with parameters
        super(IFEstimator, self).__init__(
            IFAlgorithm,
            IFProblem(n, memory_bound=memory_bound, **kwargs),
            **kwargs
        )

    def table(self, show_quantum_complexity=0, show_tilde_o_time=0,
              show_all_parameters=0, precision=1, truncate=0):
        """
        Print table describing the complexity of each algorithm and its optimal parameters

        INPUT:

        - ``show_quantum_complexity`` -- show quantum time complexity (default: False)
        - ``show_tilde_o_time`` -- show Ō time complexity (default: False)
        - ``show_all_parameters`` -- show all optimization parameters (default: False)
        - ``precision`` -- number of decimal digits output (default: 1)
        - ``truncate`` -- truncate rather than round the output (default: False)
        """
        super(IFEstimator, self).table(show_quantum_complexity=show_quantum_complexity,
                                          show_tilde_o_time=show_tilde_o_time,
                                          show_all_parameters=show_all_parameters,
                                          precision=precision, truncate=truncate)
