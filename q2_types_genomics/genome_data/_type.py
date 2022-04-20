# ----------------------------------------------------------------------------
# Copyright (c) 2022, QIIME 2 development team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------

from qiime2.plugin import SemanticType

from . import (
    GenesDirectoryFormat, ProteinsDirectoryFormat, LociDirectoryFormat
)
from ..plugin_setup import plugin

GenomeData = SemanticType('GenomeData', field_names='type')
Genes = SemanticType('Genes', variant_of=GenomeData.field['type'])
Proteins = SemanticType('Proteins', variant_of=GenomeData.field['type'])
Loci = SemanticType('Loci', variant_of=GenomeData.field['type'])

plugin.register_semantic_types(GenomeData, Genes, Proteins, Loci)

plugin.register_semantic_type_to_format(
    GenomeData[Genes],
    artifact_format=GenesDirectoryFormat
)

plugin.register_semantic_type_to_format(
    GenomeData[Proteins],
    artifact_format=ProteinsDirectoryFormat
)

plugin.register_semantic_type_to_format(
    GenomeData[Loci],
    artifact_format=LociDirectoryFormat
)
