# ----------------------------------------------------------------------------
# Copyright (c) 2022, QIIME 2 development team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------

from q2_types.feature_data import FeatureData

from q2_types_genomics.feature_data._format import MAGSequencesDirFmt
from . import ArbitraryHeaderTSVDirFmt
from qiime2.core.type import SemanticType
from ..plugin_setup import plugin


MAG = SemanticType('MAG', variant_of=FeatureData.field['type'])

plugin.register_semantic_types(MAG)
plugin.register_semantic_type_to_format(
    FeatureData[MAG],
    artifact_format=MAGSequencesDirFmt
)

# NOG stuff
NOG = SemanticType('NOG', variant_of=FeatureData.field['type'])
plugin.register_semantic_types(NOG)
plugin.register_semantic_type_to_format(
    semantic_type=FeatureData[NOG],
    artifact_format=ArbitraryHeaderTSVDirFmt
)

# KEGG stuff
KEGG = SemanticType('KEGG', variant_of=FeatureData.field['type'])
plugin.register_semantic_types(KEGG)
plugin.register_semantic_type_to_format(
        semantic_type=FeatureData[KEGG],
        artifact_format=ArbitraryHeaderTSVDirFmt
)

# OG stuff
OG = SemanticType('OG', variant_of=FeatureData.field['type'])
plugin.register_semantic_types(OG)
plugin.register_semantic_type_to_format(
        semantic_type=FeatureData[OG],
        artifact_format=ArbitraryHeaderTSVDirFmt
)
