# ----------------------------------------------------------------------------
# Copyright (c) 2022, QIIME 2 development team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------



from ..eggnog._format import EggnogRefDirFmt, EggnogOutputDirFmt, BinaryReferenceDBDirFmt, ArbitraryHeaderTSVDirFmt
#from q2_types_genomics.eggnog import EggnogRefDirFmt, EggnogOutputDirFmt, BinaryReferenceDBDirFmt
from qiime2.plugin import SemanticType, model

from ..plugin_setup import plugin




Orthologs = SemanticType('Orthologs', field_names='type')
Seed = SemanticType('Seed', variant_of=Orthologs.field['type'])

plugin.register_semantic_types(Orthologs, Seed)

plugin.register_semantic_type_to_format(
    Orthologs[Seed],
    artifact_format=EggnogOutputDirFmt)

OrthologDirFmt = model.SingleFileDirectoryFormat(
                     'OrthologDirFmt',
                     'orthologs.tsv',
                     ArbitraryHeaderTSVDirFmt)

# TODO: ortholog validator

# FROM ORIGINAL DEFINITION IN FEATURE DATA

# NOG stuff
Annotation = SemanticType('Annotation', field_names='type')

plugin.register_semantic_types(Annotation)

NOG = SemanticType('NOG', variant_of=Annotation.field['type'])
plugin.register_semantic_types(NOG)
plugin.register_semantic_type_to_format(
    semantic_type=Annotation[NOG],
    artifact_format=ArbitraryHeaderTSVDirFmt
)

# KEGG stuff
KEGG = SemanticType('KEGG', variant_of=Annotation.field['type'])
plugin.register_semantic_types(KEGG)
plugin.register_semantic_type_to_format(
        semantic_type=Annotation[KEGG],
        artifact_format=ArbitraryHeaderTSVDirFmt
)

# OG stuff
OG = SemanticType('OG', variant_of=Annotation.field['type'])
plugin.register_semantic_types(OG)
plugin.register_semantic_type_to_format(
        semantic_type=Annotation[OG],
        artifact_format=ArbitraryHeaderTSVDirFmt
)

# types for downloading the databases eggnogmapper is using.

ReferenceDB = SemanticType('ReferenceDB', field_names='type')
Eggnog = SemanticType('Eggnog', variant_of=ReferenceDB.field['type'])
plugin.register_semantic_types(ReferenceDB, Eggnog)
plugin.register_semantic_type_to_format(
    ReferenceDB[Eggnog],
    artifact_format=BinaryReferenceDBDirFmt
    )

DiamondDB = SemanticType('DiamondDB', variant_of=ReferenceDB.field['type'])
plugin.register_semantic_types(DiamondDB)
plugin.register_semantic_type_to_format(
        ReferenceDB[DiamondDB],
        artifact_format=BinaryReferenceDBDirFmt
)

MMseq2DB = SemanticType('MMseq2DB', variant_of=ReferenceDB.field['type'])
plugin.register_semantic_types(MMseq2DB)
plugin.register_semantic_type_to_format(
        ReferenceDB[MMseq2DB],
        artifact_format=BinaryReferenceDBDirFmt
)

EggnogDB = SemanticType('EggnogDB', variant_of=ReferenceDB.field['type'])
plugin.register_semantic_types(EggnogDB)
plugin.register_semantic_type_to_format(
         EggnogDB,
         artifact_format=BinaryReferenceDBDirFmt
 )
