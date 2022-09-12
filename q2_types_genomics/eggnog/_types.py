# ----------------------------------------------------------------------------
# Copyright (c) 2022, QIIME 2 development team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------


from ..eggnog._format import EggnogRefDirFmt, EggnogOutputDirFmt
from qiime2.plugin import SemanticType
from ..plugin_setup import plugin

ReferenceDB = SemanticType('ReferenceDB', field_names='type')

Eggnog = SemanticType('Eggnog', variant_of=ReferenceDB.field['type'])

plugin.register_semantic_types(ReferenceDB, Eggnog)

plugin.register_semantic_type_to_format(
    ReferenceDB[Eggnog],
    artifact_format=EggnogRefDirFmt
)
