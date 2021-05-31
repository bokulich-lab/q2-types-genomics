# ----------------------------------------------------------------------------
# Copyright (c) 2021, QIIME 2 development team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------

import importlib

from ._format import (
    GenesDirectoryFormat, ProteinsDirectoryFormat, LociDirectoryFormat
)
from ._type import (
    GenomeData, Genes, Proteins, Loci
)

__all__ = [
    'GenomeData', 'Genes', 'Proteins', 'Loci',
    'GenesDirectoryFormat', 'ProteinsDirectoryFormat', 'LociDirectoryFormat'
]

importlib.import_module('q2_types_genomics.genome_data._transformer')
