# ----------------------------------------------------------------------------
# Copyright (c) 2021, QIIME 2 development team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------

from qiime2.plugin import SemanticType

from ..plugin_setup import plugin
from . import GenesDirectoryFormat, ProteinsDirectoryFormat


GenomeData = SemanticType('GenomeData', field_names='type')
Genes = SemanticType('Genes', variant_of=GenomeData.field['type'])
Proteins = SemanticType('Proteins', variant_of=GenomeData.field['type'])

plugin.register_semantic_types(GenomeData, Genes, Proteins)

plugin.register_semantic_type_to_format(
    GenomeData[Genes],
    artifact_format=GenesDirectoryFormat
)

plugin.register_semantic_type_to_format(
    GenomeData[Proteins],
    artifact_format=ProteinsDirectoryFormat
)
