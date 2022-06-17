# ----------------------------------------------------------------------------
# Copyright (c) 2021, QIIME 2 development team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------

from qiime2.plugin import SemanticType
from q2_types.feature_data import FeatureData

from q2_types_genomics.eggnog._format import FunctionalAnnotationDirFmt

from ..plugin_setup import plugin

NOG = SemanticType('NOG', variant_of=FeatureData.field['type'])

plugin.register_semantic_types(NOG)

plugin.register_semantic_type_to_format(
    semantic_type=FeatureData[NOG],
    artifact_format= FunctionalAnnotationDirFmt
)
