# ----------------------------------------------------------------------------
# Copyright (c) 2023, QIIME 2 development team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------

from q2_types.feature_data import FeatureData

from q2_types_genomics.feature_data._format import MAGSequencesDirFmt
from qiime2.core.type import SemanticType

from ..plugin_setup import plugin


MAG = SemanticType('MAG', variant_of=FeatureData.field['type'])

plugin.register_semantic_types(MAG)
plugin.register_semantic_type_to_format(
    FeatureData[MAG],
    artifact_format=MAGSequencesDirFmt
)
