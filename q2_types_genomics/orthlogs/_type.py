
Ortholog = SemanticType('Ortholog', field_names='type')
Seed = SemanticType('Seed', variant_of=Orthologs.field['type'])

plugin.register_semantic_types(Ortholog, Seed)

