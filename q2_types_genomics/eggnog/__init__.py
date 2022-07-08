# ----------------------------------------------------------------------------
# Copyright (c) 2021-2022, QIIME 2 development team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------

import importlib
from ._type import (
    NOG, KEGG, OG,
)

from ._format import (
    ArbitraryHeaderTSVFmt, ArbitraryHeaderTSVDirFmt
)

importlib.import_module('q2_types_genomics.eggnog._transformer')
importlib.import_module('q2_types_genomics.eggnog._validator')


__all__ = [
    'NOG', 'ArbitraryHeaderTSVFmt', 'ArbitraryHeaderTSVDirFmt', 'KEGG', 'OG',
]
