from qiime2.plugin import SemanticType, model
from q2_types_genomics.diamond import DiamondDatabaseDirFmt, DiamondDatabaseFileFmt, OrthologDirFmt
from q2_types_genomics.plugin_setup import plugin

ReferenceDB = SemanticType('ReferenceDB', field_names="type")
Diamond = SemanticType('Diamond', variant_of='ReferenceDB')
plugin.register_semantic_types(ReferenceDB, Diamond)

Orthologs = SemanticType('Orthologs', field_names='type')
Seed = SemanticType('Seed', variant_of=Orthologs.field['type'])

plugin.register_semantic_types(Orthologs, Seed)

plugin.register_semantic_type_to_format(
    Orthologs[Seed],
    artifact_format=OrthologDirFmt)

OrthologDirFmt = model.SingleFileDirectoryFormat(
                     'OrthologDirFmt',
                     'orthologs.tsv',
                     ArbitraryHeaderTSVDirFmt)
