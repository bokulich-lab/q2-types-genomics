# ----------------------------------------------------------------------------
# Copyright (c) 2022, QIIME 2 development team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------
from q2_types.sample_data import SampleData
from qiime2.plugin import SemanticType

from . import (
    Kraken2ReportDirectoryFormat, Kraken2OutputDirectoryFormat
)
from ..plugin_setup import plugin


Kraken2Reports = SemanticType(
    'Kraken2Report', variant_of=SampleData.field['type']
)
Kraken2Outputs = SemanticType(
    'Kraken2Output', variant_of=SampleData.field['type']
)


plugin.register_semantic_types(Kraken2Reports, Kraken2Outputs)

plugin.register_semantic_type_to_format(
    SampleData[Kraken2Reports],
    artifact_format=Kraken2ReportDirectoryFormat
)
plugin.register_semantic_type_to_format(
    SampleData[Kraken2Outputs],
    artifact_format=Kraken2OutputDirectoryFormat
)
