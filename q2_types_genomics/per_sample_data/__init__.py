# ----------------------------------------------------------------------------
# Copyright (c) 2021, QIIME 2 development team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------

import importlib

from ._format import (
    MAGSequencesDirFmt, MultiMAGManifestFormat, ContigSequencesDirFmt
)
from ._type import (
    MAGs, Contigs
)

__all__ = [
    'MAGs', 'MAGSequencesDirFmt', 'MultiMAGManifestFormat',
    'ContigSequencesDirFmt', 'Contigs'
]

importlib.import_module('q2_types_genomics.per_sample_data._transformer')
