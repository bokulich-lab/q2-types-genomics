# ----------------------------------------------------------------------------
# Copyright (c) 2021, QIIME 2 development team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------

from q2_types.feature_data import DNAFASTAFormat, ProteinFASTAFormat
import qiime2.plugin.model as model

from ..plugin_setup import plugin

GenesDirectoryFormat = model.SingleFileDirectoryFormat(
    'GenesDirectoryFormat',
    r'genes[0-9]+\.(fa|fasta)$',
    DNAFASTAFormat
)

ProteinsDirectoryFormat = model.SingleFileDirectoryFormat(
    'ProteinsDirectoryFormat',
    r'proteins[0-9]+\.(fa|faa|fasta)$',
    ProteinFASTAFormat
)

plugin.register_formats(GenesDirectoryFormat, ProteinsDirectoryFormat)
