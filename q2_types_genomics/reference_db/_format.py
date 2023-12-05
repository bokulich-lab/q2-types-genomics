# ----------------------------------------------------------------------------
# Copyright (c) 2023, QIIME 2 development team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------


from qiime2.plugin import model
from q2_types_genomics.plugin_setup import plugin
from q2_types_genomics.reference_db._type import (
    ReferenceDB, Eggnog, Diamond, EggnogSequenceTaxa
)
from q2_types.feature_data import ProteinFASTAFormat


class EggnogRefTextFileFmt(model.TextFileFormat):
    def _validate_(self, level):
        # TODO: have native diamond validation run on db/self.path
        pass


class EggnogRefBinFileFmt(model.BinaryFileFormat):
    def _validate_(self, level):
        pass


plugin.register_formats(EggnogRefTextFileFmt, EggnogRefBinFileFmt)


class EggnogRefDirFmt(model.DirectoryFormat):
    eggnog = model.FileCollection(r'eggnog.*db.*',
                                  format=EggnogRefBinFileFmt)

    @eggnog.set_path_maker
    def eggnog_path_maker(self, name):
        return str(name)


plugin.register_formats(EggnogRefDirFmt)

plugin.register_semantic_type_to_format(
        ReferenceDB[Eggnog],
        EggnogRefDirFmt)


class DiamondDatabaseFileFmt(model.BinaryFileFormat):
    def _validate_(self, level):
        # TODO: have native diamond validation run on db/self.path
        pass


DiamondDatabaseDirFmt = model.SingleFileDirectoryFormat(
    'DiamondDatabaseDirFmt', 'ref_db.dmnd', DiamondDatabaseFileFmt)

plugin.register_formats(DiamondDatabaseFileFmt, DiamondDatabaseDirFmt)
plugin.register_semantic_type_to_format(ReferenceDB[Diamond],
                                        DiamondDatabaseDirFmt)


class EggnogSequenceTaxaDirFmt(model.DirectoryFormat):
    taxid_info = model.File("e5.taxid_info.tsv", format=EggnogRefTextFileFmt)
    faa = model.File("e5.proteomes.faa", format=ProteinFASTAFormat)


plugin.register_formats(EggnogSequenceTaxaDirFmt)
plugin.register_semantic_type_to_format(ReferenceDB[EggnogSequenceTaxa],
                                        EggnogSequenceTaxaDirFmt)
