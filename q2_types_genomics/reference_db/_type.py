from qiime2.plugin import SemanticType, model
from q2_types_genomics.plugin_setup import plugin

ReferenceDB = SemanticType('ReferenceDB', field_names='type')
Diamond = SemanticType('Diamond', variant_of=ReferenceDB.field['type'])
Eggnog = SemanticType('Eggnog', variant_of=ReferenceDB.field['type'])

plugin.register_semantic_types(ReferenceDB, Diamond, Eggnog)
