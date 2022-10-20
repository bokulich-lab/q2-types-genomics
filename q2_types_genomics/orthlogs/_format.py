from qiime2.plugin import model
from q2_types_genomics.orthlogs import Ortholog, Seed
from q2_types_genomics.plugin_setup import plugin

class OrthologFileFmt(model.TextFileFormat):
    def _validate_(self, level):
        pass

OrthologDirFmt = model.SingleFileDirectoryFormat(
                     'OrthologDirFmt',
                     'orthologs.tsv',
                     OrthologFileFmt)

plugin.register_formats(OrthologFileFmt, OrthologDirFmt)

plugin.register_semantic_type_to_format(
    Ortholog[Seed],
    artifact_format=OrthologDirFmt)
