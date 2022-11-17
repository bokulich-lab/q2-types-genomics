# ----------------------------------------------------------------------------
# Copyright (c) 2022, QIIME 2 development team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------

import importlib

from ._format import (
    Kraken2ReportFormat
)
# from ._transformer import IntervalMetadataIterator
# from ._type import (
#     GenomeData, Genes, Proteins, Loci
# )

__all__ = [
    'Kraken2ReportFormat'
]

# importlib.import_module('q2_types_genomics.kraken2._transformer')
