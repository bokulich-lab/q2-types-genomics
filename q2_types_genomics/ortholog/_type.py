# ----------------------------------------------------------------------------
# Copyright (c) 2022, QIIME 2 development team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------


from qiime2.plugin import SemanticType
from q2_types_genomics.plugin_setup import plugin

Ortholog = SemanticType('Ortholog', field_names='type')
Seed = SemanticType('Seed', variant_of=Ortholog.field['type'])
Annotation = SemanticType('Annotation', variant_of=Ortholog.field['type'])

plugin.register_semantic_types(Ortholog, Seed, Annotation)
