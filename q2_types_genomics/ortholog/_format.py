from qiime2.plugin import model
from q2_types_genomics.eggnog import EggnogRefTextFileFmt, EggnogRefBinFileFmt
from q2_types_genomics.ortholog import Ortholog, Seed
from q2_types_genomics.plugin_setup import plugin

class OrthologFileFmt(model.TextFileFormat):
    def _validate_(self, level):
        pass

# OrthologDirFmt = model.SingleFileDirectoryFormat(
#                      'OrthologDirFmt',
#                      'orthologs.tsv',
#                      OrthologFileFmt)

class OrthologDirFmt(model.DirectoryFormat):
     annotations = model.File(r".*\..*\.annotations",
                             format=EggnogRefBinFileFmt)

     gene_pred_seqs = model.File(r".*\.*\.genepred\.fasta",
                                 format=EggnogRefTextFileFmt
                                 )

     gene_pred_gff = model.File(r".*\..*\.genepred.gff",
                                format=EggnogRefTextFileFmt
                                )

     seed_orthologs = model.File(r".*\..*\.seed_orthologs",
                                 format=EggnogRefTextFileFmt
                                 )



plugin.register_formats(OrthologFileFmt, OrthologDirFmt)

plugin.register_semantic_type_to_format(
    Ortholog[Seed],
    artifact_format=OrthologDirFmt)
