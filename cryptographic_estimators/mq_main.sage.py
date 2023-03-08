# ****************************************************************************
# 		Copyright 2023 Technology Innovation Institute
# 
# 	This program is free software: you can redistribute it and/or modify
# 	it under the terms of the GNU General Public License as published by
# 	the Free Software Foundation, either version 3 of the License, or
# 	(at your option) any later version.
# 
# 	This program is distributed in the hope that it will be useful,
# 	but WITHOUT ANY WARRANTY; without even the implied warranty of
# 	MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# 	GNU General Public License for more details.
# 
# 	You should have received a copy of the GNU General Public License
# 	along with this program.  If not, see <https://www.gnu.org/licenses/>.
# ****************************************************************************
 




# This file was *autogenerated* from the file mq_main.sage
from sage.all_cmdline import *   # import sage library

_sage_const_15 = Integer(15); _sage_const_2 = Integer(2)
from MQEstimator.mq_estimator import MQEstimator
from MQEstimator.mq_problem import MQProblem

from MQEstimator.MQAlgorithms.boolean_solve_fxl import BooleanSolveFXL
from MQEstimator.MQAlgorithms.bjorklund import Bjorklund
from MQEstimator.MQAlgorithms.cgmta import CGMTA
from MQEstimator.MQAlgorithms.crossbred import Crossbred
from MQEstimator.MQAlgorithms.dinur1 import DinurFirst
from MQEstimator.MQAlgorithms.dinur2 import DinurSecond
from MQEstimator.MQAlgorithms.exhaustive_search import ExhaustiveSearch
from MQEstimator.MQAlgorithms.f5 import F5
from MQEstimator.MQAlgorithms.hybrid_f5 import HybridF5
from MQEstimator.MQAlgorithms.kpg import KPG
from MQEstimator.MQAlgorithms.lokshtanov import Lokshtanov
from MQEstimator.MQAlgorithms.mht import MHT

E = MQEstimator(n=_sage_const_15 , m=_sage_const_15 , q=_sage_const_2 )
E.table()


