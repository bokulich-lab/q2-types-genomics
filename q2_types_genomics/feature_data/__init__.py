# ----------------------------------------------------------------------------
# Copyright (c) 2021, QIIME 2 development team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------

import importlib

from ._format import MAGSequencesDirFmt
from ._type import MAG
from ._transformer import MAGIterator

__all__ = [
    'MAG', 'MAGSequencesDirFmt', 'MAGIterator'
]

importlib.import_module('q2_types_genomics.feature_data._transformer')
