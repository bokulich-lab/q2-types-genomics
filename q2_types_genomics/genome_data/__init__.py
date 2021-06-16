# ----------------------------------------------------------------------------
# Copyright (c) 2021, QIIME 2 development team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------

import importlib

from ._format import GenesDirectoryFormat, ProteinsDirectoryFormat
from ._type import GenomeData, Genes, Proteins

__all__ = [
    'GenomeData', 'Genes', 'Proteins',
    'GenesDirectoryFormat', 'ProteinsDirectoryFormat'
]

importlib.import_module('q2_types_genomics.genome_data._transformer')
