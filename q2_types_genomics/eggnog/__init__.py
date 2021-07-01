# ----------------------------------------------------------------------------
# Copyright (c) 2021, QIIME 2 development team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------

from ._type import NOG

from ._format import (
    EggnogFmt, EggnogDirFmt, HeaderlessEggnogFmt,
)

__all__ = [
    'NOG', 'EggnogFmt', 'HeaderlessEggnogFmt', 'EggnogDirFmt',
]
