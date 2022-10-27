from qiime2.plugin import model
from q2_types_genomics.plugin_setup import plugin
from q2_types_genomics.reference_db import ReferenceDB, Eggnog

class EggnogRefTextFileFmt(model.TextFileFormat):
    def _validate_(self, level):
        # TODO: have native diamond validation run on db/self.path
        pass

class EggnogRefBinFileFmt(model.BinaryFileFormat):
    def _validate_(self, level):
        pass

plugin.register_formats(EggnogRefTextFileFmt, EggnogRefBinFileFmt)

#EggnogRefDirFmt = model.SingleFileDirectoryFormat('EggnogRefDirFmt', 'eggnog.db', EggnogRefFileFmt)
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
