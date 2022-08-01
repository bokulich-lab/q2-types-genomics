# ----------------------------------------------------------------------------
# Copyright (c) 2022, QIIME 2 development team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------

import importlib

from ._format import (
    ArbitraryHeaderTSVFmt, ArbitraryHeaderTSVDirFmt, MAGSequencesDirFmt,
)
from ._type import (
    NOG, KEGG, OG, MAG, DiamondDB, MMseq2DB,
)
from ._transformer import MAGIterator

__all__ = [
    'MAG', 'MAGSequencesDirFmt', 'MAGIterator', 'NOG',
    'ArbitraryHeaderTSVFmt', 'ArbitraryHeaderTSVDirFmt', 'KEGG', 'OG',
    'DiamondDB', 'MMseq2DB',
]

importlib.import_module('q2_types_genomics.feature_data._transformer')
importlib.import_module('q2_types_genomics.feature_data._validator')
