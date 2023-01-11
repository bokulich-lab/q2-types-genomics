# ----------------------------------------------------------------------------
# Copyright (c) 2023, QIIME 2 development team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------

import importlib

from ._format import (
    GenesDirectoryFormat, ProteinsDirectoryFormat,
    GFF3Format, LociDirectoryFormat
)
from ._transformer import IntervalMetadataIterator
from ._type import (
    GenomeData, Genes, Proteins, Loci
)

__all__ = [
    'GenomeData', 'Genes', 'Proteins', 'Loci', 'GFF3Format',
    'GenesDirectoryFormat', 'ProteinsDirectoryFormat', 'LociDirectoryFormat',
    'IntervalMetadataIterator'
]

importlib.import_module('q2_types_genomics.genome_data._transformer')
