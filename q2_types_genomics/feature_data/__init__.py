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
    BinaryReferenceDBFmt, BinaryReferenceDBDirFmt, EggnogRefBinFileFmt,
    EggnogRefTextFileFmt, EggnogRefDirFmt,
)

from ._type import (
    NOG, KEGG, OG, MAG, DiamondDB, MMseq2DB, EggnogDB,
)
from ._transformer import MAGIterator

__all__ = [
    'MAG', 'MAGSequencesDirFmt', 'MAGIterator', 'NOG',
    'ArbitraryHeaderTSVFmt', 'ArbitraryHeaderTSVDirFmt', 'KEGG', 'OG',
    'DiamondDB', 'MMseq2DB', 'BinaryReferenceDBFmt',
    'BinaryReferenceDBDirFmt', 'EggnogDB', 'EggnogRefBinFileFmt',
    'EggnogRefTextFileFmt', 'EggnogRefDirFmt',
]

importlib.import_module('q2_types_genomics.feature_data._transformer')
importlib.import_module('q2_types_genomics.feature_data._validator')
