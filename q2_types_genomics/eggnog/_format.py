from qiime2.plugin import model
from q2_types_genomics.plugin_setup import plugin
from q2_types_genomics.reference_db import ReferenceDB, Eggnog

class EggnogRefFileFmt(model.BinaryFileFormat):
    def _validate_(self, level):
        # TODO: have native diamond validation run on db/self.path
        pass

EggnogRefDirFmt = model.SingleFileDirectoryFormat('EggnogRefDirFmt', 'ref_db.dmnd', EggnogRefFileFmt)
plugin.register_formats(EggnogRefFileFmt, EggnogRefDirFmt)
plugin.register_semantic_type_to_format(EggnogRefDirFmt, ReferenceDB[Eggnog])
