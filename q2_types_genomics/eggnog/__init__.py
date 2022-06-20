# ----------------------------------------------------------------------------
# Copyright (c) 2021-2022, QIIME 2 development team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------

from ._type import NOG

from ._format import (
    EggnogAnnotationFmt, EggnogAnnotationDirFmt
)
from q2_types.feature_data import FeatureData
from ..plugin_setup import plugin

plugin.register_semantic_type_to_format(
    semantic_type=FeatureData[NOG],
    artifact_format=EggnogAnnotationDirFmt
)

__all__ = [
    'NOG', 'EggnogAnnotationFmt', 'EggnogAnnotationDirFmt',
]
