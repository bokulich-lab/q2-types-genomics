from qiime2.plugin import model

class OrthologFileFmt(model.TextFileFormat):
    pass

OrthologDirFmt = model.SingleFileDirectoryFormat(
                     'OrthologDirFmt',
                     'orthologs.tsv',
                     OrthologFileFmt)

plugin.register_semantic_type_to_format(
    Orthologs[Seed],
    artifact_format=OrthologDirFmt)
