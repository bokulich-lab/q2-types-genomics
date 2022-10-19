from qiime2.plugin import model
from q2_types_genomics.plugin_setup import plugin

class DiamondDatabaseFileFmt(model.BinaryFileFormat):
    def _validate_(self, level):
        # TODO: have native diamond validation run on db/self.path
        pass

DiamondDatabaseDirFmt = model.SingleFileDirectoryFormat('DiamondDatabaseDirFmt', 'ref_db.dmnd', DiamondDatabaseFileFmt)
plugin.register_formats(DiamondDatabaseFileFmt, DiamondDatabaseDirFmt)
