from qiime2.plugin import SemanticType
from q2_types_genomics.plugin_setup import plugin

Ortholog = SemanticType('Ortholog', field_names='type')
Seed = SemanticType('Seed', variant_of=Ortholog.field['type'])

plugin.register_semantic_types(Ortholog, Seed)
