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


from enum import Enum

SDFQ_CODE_LENGTH = "code length"
SDFQ_CODE_DIMENSION = "code dimension"
SDFQ_ERROR_WEIGHT = "error weight"
SDFQ_ERROR_FIELD_SIZE = "field size"


class VerboseInformation(Enum):
    CONSTRAINTS = "constraints"
    PERMUTATIONS = "permutations"
    TREE = "tree"
    GAUSS = "gauss"
    REPRESENTATIONS = "representation"
    LISTS = "lists"
